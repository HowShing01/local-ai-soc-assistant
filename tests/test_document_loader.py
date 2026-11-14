
import tempfile
import unittest

from pathlib import Path
from docx import Document as DocxDocument

from src.rag.document_loader import (
    load_file,
    load_knowledge_base
)


class TestDocumentLoader(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_load_txt(self):
        file_path = self.base_dir / "sample.txt"
        file_path.write_text(
            "This is a cybersecurity test.",
            encoding="utf-8"
        )

        documents = load_file(file_path, self.base_dir)

        self.assertEqual(len(documents), 1)
        self.assertIn(
            "cybersecurity",
            documents[0]["content"]
        )
        self.assertEqual(
            documents[0]["metadata"]["file_type"],
            "txt"
        )

    def test_load_docx(self):
        file_path = self.base_dir / "sample.docx"

        doc = DocxDocument()
        doc.add_paragraph("Incident response procedure")
        doc.save(file_path)

        documents = load_file(file_path, self.base_dir)

        self.assertEqual(len(documents), 1)
        self.assertIn(
            "Incident response",
            documents[0]["content"]
        )

    def test_load_csv(self):
        file_path = self.base_dir / "sample.csv"

        file_path.write_text(
            "CVE,Severity\nCVE-2026-1234,High\n",
            encoding="utf-8"
        )

        documents = load_file(file_path, self.base_dir)

        self.assertEqual(len(documents), 1)
        self.assertIn(
            "CVE-2026-1234",
            documents[0]["content"]
        )
        self.assertIn(
            "Severity: High",
            documents[0]["content"]
        )

    def test_unsupported_file(self):
        file_path = self.base_dir / "sample.exe"
        file_path.write_text("test", encoding="utf-8")

        with self.assertRaises(ValueError):
            load_file(file_path, self.base_dir)

    def test_load_knowledge_base(self):
        file_path = self.base_dir / "sample.txt"
        file_path.write_text(
            "MITRE ATT&CK testing",
            encoding="utf-8"
        )

        documents, errors = load_knowledge_base(self.base_dir)

        self.assertEqual(len(documents), 1)
        self.assertEqual(len(errors), 0)


if __name__ == "__main__":
    unittest.main()

