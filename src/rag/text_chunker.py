
DEFAULT_CHUNK_SIZE = 800
DEFAULT_CHUNK_OVERLAP = 150


def _validate_parameters(chunk_size, overlap):
    """Validate chunking configuration."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")


def _split_text_with_offsets(text, chunk_size, overlap):
    """Split text into overlapping chunks with character offsets."""
    _validate_parameters(chunk_size, overlap)

    if not text or not text.strip():
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        chunk_content = text[start:end].strip()

        if chunk_content:
            chunks.append((chunk_content, start, end))

        if end >= len(text):
            break

        start = end - overlap

    return chunks


def chunk_text(
    text,
    chunk_size=DEFAULT_CHUNK_SIZE,
    overlap=DEFAULT_CHUNK_OVERLAP
):
    """Split a text string into overlapping chunks."""
    chunks = _split_text_with_offsets(
        text,
        chunk_size,
        overlap
    )

    return [content for content, _, _ in chunks]


def chunk_document(
    document,
    chunk_size=DEFAULT_CHUNK_SIZE,
    overlap=DEFAULT_CHUNK_OVERLAP
):
    """Split one document while preserving its metadata."""
    if not isinstance(document, dict):
        raise TypeError("document must be a dictionary")

    content = document.get("content")
    metadata = document.get("metadata", {})

    if not isinstance(content, str):
        raise ValueError("document content must be a string")

    if not isinstance(metadata, dict):
        raise ValueError("document metadata must be a dictionary")

    chunks = _split_text_with_offsets(
        content,
        chunk_size,
        overlap
    )

    results = []

    for index, (chunk_content, start, end) in enumerate(chunks):
        chunk_metadata = metadata.copy()

        chunk_metadata.update({
            "chunk_index": index,
            "chunk_start": start,
            "chunk_end": end
        })

        results.append({
            "content": chunk_content,
            "metadata": chunk_metadata
        })

    return results


def chunk_documents(
    documents,
    chunk_size=DEFAULT_CHUNK_SIZE,
    overlap=DEFAULT_CHUNK_OVERLAP
):
    """Split multiple documents into chunks."""
    results = []

    for document in documents:
        results.extend(
            chunk_document(
                document,
                chunk_size=chunk_size,
                overlap=overlap
            )
        )

    return results
