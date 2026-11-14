
import unittest

from src.rag.text_chunker import (
    chunk_text,
    chunk_document,
    chunk_documents
)


class TestTextChunker(unittest.TestCase):

    def test_empty_text(self):
        self.assertEqual(chunk_text(""), [])

    def test_short_text(self):
        text = "This is a short cybersecurity document."

        chunks = chunk_text(text)

        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0], text)

    def test_chunk_size(self):
        text = "A" * 25

        chunks = chunk_text(
            text,
            chunk_size=10,
            overlap=2
        )

        self.assertTrue(
            all(len(chunk) <= 10 for chunk in chunks)
        )

    def test_chunk_overlap(self):
        text = "A" * 25

        chunks = chunk_text(
            text,
            chunk_size=10,
            overlap=3
        )

        self.assertEqual(chunks[0][-3:], chunks[1][:3])

    def test_metadata_preservation(self):
        document = {
            "content": "A" * 25,
            "metadata": {
                "file_name": "mitre.txt",
                "file_type": "txt",
                "source": "mitre_attack/mitre.txt"
            }
        }

        chunks = chunk_document(
            document,
            chunk_size=10,
            overlap=2
        )

        self.assertGreater(len(chunks), 1)

        self.assertEqual(
            chunks[0]["metadata"]["file_name"],
            "mitre.txt"
        )

        self.assertEqual(
            chunks[0]["metadata"]["chunk_index"],
            0
        )

        self.assertEqual(
            chunks[1]["metadata"]["chunk_index"],
            1
        )

    def test_multiple_documents(self):
        documents = [
            {
                "content": "A" * 20,
                "metadata": {"file_name": "file1.txt"}
            },
            {
                "content": "B" * 20,
                "metadata": {"file_name": "file2.txt"}
            }
        ]

        chunks = chunk_documents(
            documents,
            chunk_size=10,
            overlap=2
        )

        self.assertEqual(len(chunks), 6)

    def test_invalid_chunk_size(self):
        with self.assertRaises(ValueError):
            chunk_text("Testing", chunk_size=0)

    def test_invalid_overlap(self):
        with self.assertRaises(ValueError):
            chunk_text(
                "Testing",
                chunk_size=10,
                overlap=10
            )


if __name__ == "__main__":
    unittest.main()
