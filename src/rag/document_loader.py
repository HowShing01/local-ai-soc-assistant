
from pathlib import Path
from typing import Any

import pandas as pd
from docx import Document as DocxDocument
from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".docx", ".csv"}


def create_document(content: str, metadata: dict[str, Any]) -> dict:
    """Create a standard document record for the RAG pipeline."""
    return {
        "content": content,
        "metadata": metadata
    }


def load_pdf(file_path: Path, base_dir: Path) -> list[dict]:
    """Extract text from a PDF, keeping each page as a separate document."""
    documents = []
    reader = PdfReader(str(file_path))

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        text = text.strip()

        if not text:
            continue

        documents.append(
            create_document(
                content=text,
                metadata={
                    "file_name": file_path.name,
                    "file_type": "pdf",
                    "source": file_path.relative_to(base_dir).as_posix(),
                    "page_number": page_number
                }
            )
        )

    return documents


def load_txt(file_path: Path, base_dir: Path) -> list[dict]:
    """Read a UTF-8 text file."""
    text = file_path.read_text(
        encoding="utf-8-sig",
        errors="replace"
    ).strip()

    if not text:
        return []

    return [
        create_document(
            content=text,
            metadata={
                "file_name": file_path.name,
                "file_type": "txt",
                "source": file_path.relative_to(base_dir).as_posix()
            }
        )
    ]


def load_docx(file_path: Path, base_dir: Path) -> list[dict]:
    """Extract paragraphs and tables from a DOCX file."""
    doc = DocxDocument(str(file_path))

    text_parts = []

    # Extract normal paragraphs
    for paragraph in doc.paragraphs:
        paragraph_text = paragraph.text.strip()

        if paragraph_text:
            text_parts.append(paragraph_text)

    # Extract table content
    for table in doc.tables:
        for row in table.rows:
            row_text = " | ".join(
                cell.text.strip() for cell in row.cells
            )

            if row_text.strip(" |"):
                text_parts.append(row_text)

    text = "\n".join(text_parts).strip()

    if not text:
        return []

    return [
        create_document(
            content=text,
            metadata={
                "file_name": file_path.name,
                "file_type": "docx",
                "source": file_path.relative_to(base_dir).as_posix()
            }
        )
    ]


def load_csv(file_path: Path, base_dir: Path) -> list[dict]:
    """Read CSV data and convert each row into a text document."""
    dataframe = pd.read_csv(
        file_path,
        dtype=str,
        keep_default_na=False,
        encoding="utf-8-sig"
    )

    documents = []

    for row_index, row in dataframe.iterrows():
        row_parts = []

        for column_name, value in row.items():
            value = str(value).strip()

            if value:
                row_parts.append(f"{column_name}: {value}")

        if not row_parts:
            continue

        content = "\n".join(row_parts)

        documents.append(
            create_document(
                content=content,
                metadata={
                    "file_name": file_path.name,
                    "file_type": "csv",
                    "source": file_path.relative_to(base_dir).as_posix(),
                    "row_number": int(row_index) + 1
                }
            )
        )

    return documents


def load_file(file_path: Path, base_dir: Path) -> list[dict]:
    """Load one supported file based on its extension."""
    extension = file_path.suffix.lower()

    loaders = {
        ".pdf": load_pdf,
        ".txt": load_txt,
        ".docx": load_docx,
        ".csv": load_csv
    }

    if extension not in loaders:
        raise ValueError(f"Unsupported file format: {extension}")

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    return loaders[extension](file_path, base_dir)


def load_knowledge_base(
    knowledge_base_dir: str | Path
) -> tuple[list[dict], list[dict]]:
    """
    Recursively load supported files from the knowledge base.

    Returns:
        documents: Successfully extracted documents.
        errors: Files that could not be processed.
    """
    base_dir = Path(knowledge_base_dir).resolve()

    if not base_dir.exists():
        raise FileNotFoundError(
            f"Knowledge base directory not found: {base_dir}"
        )

    if not base_dir.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {base_dir}"
        )

    documents = []
    errors = []

    for file_path in sorted(base_dir.rglob("*")):
        if not file_path.is_file():
            continue

        if file_path.name.startswith("."):
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        try:
            loaded_documents = load_file(file_path, base_dir)
            documents.extend(loaded_documents)

            if not loaded_documents:
                errors.append({
                    "file": str(file_path.relative_to(base_dir)),
                    "error": "No extractable text found"
                })

        except Exception as error:
            errors.append({
                "file": str(file_path.relative_to(base_dir)),
                "error": str(error)
            })

    return documents, errors
