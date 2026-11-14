# local-ai-soc-assistant


## Team Branch Assignment

| Name | Assigned Branch | Switch Command |
|---|---|---|
| Ashton | `feature/app-security` | `git switch feature/app-security` |
| Ruizhe | `feature/data-security` | `git switch feature/data-security` |
| How Shing | `feature/rag` | `git switch feature/rag` |



## Common Git Operations

| Operation | Git Command |
|---|---|
| Check current branch | `git branch --show-current` |
| Check changes | `git status` |
| Stage changes | `git add .` |
| Commit changes | `git commit -m "Describe changes"` |
| Push branch | `git push` |
| Fetch remote updates | `git fetch origin` |
| Update local branch | `git pull` |





## 📁 Project Directory Structure

The project is organised into several directories to separate cybersecurity knowledge resources, application components, RAG implementation, security mechanisms, and testing files.

### Overall Directory Structure

```text
local-ai-soc/
│
├── knowledge_base/
│   ├── mitre_attack/
│   ├── cisa_playbooks/
│   ├── csa_singapore/
│   └── nvd/
│
├── logs/
│
├── src/
│   ├── app/
│   │   └── streamlit_app.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── document_loader.py
│   │   ├── text_chunker.py
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── generator.py
│   │
│   ├── security/
│   │   ├── input_validation.py
│   │   └── output_validation.py
│   │
│   ├── config/
│   │   └── settings.py
│   │
│   └── main.py
│
├── storage/
│
├── tests/
│   ├── test_document_loader.py
│   ├── test_text_chunker.py
│   ├── test_embeddings.py
│   └── test_retrieval.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

### 1. `knowledge_base/`

Stores cybersecurity reference documents and knowledge resources used by the Retrieval-Augmented Generation (RAG) system.

- **`mitre_attack/`** – Stores MITRE ATT&CK resources, including information about adversary tactics, techniques, and procedures (TTPs).
- **`cisa_playbooks/`** – Stores CISA cybersecurity incident response playbooks and related guidance.
- **`csa_singapore/`** – Stores cybersecurity guidelines, advisories, and resources from the Cyber Security Agency of Singapore (CSA).
- **`nvd/`** – Stores relevant vulnerability information and reference data from the National Vulnerability Database (NVD).

### 2. `logs/`

Stores application and system log files generated during development and execution.

These logs help developers troubleshoot errors, monitor application activities, and investigate unexpected behaviour.

### 3. `src/`

Contains the main source code of the Local AI SOC Assistant.

#### 3.1 `app/`

Contains the application interface and user interaction components.

- **`streamlit_app.py`** – Provides the Streamlit-based user interface for interacting with the Local AI SOC Assistant.

#### 3.2 `rag/`

Contains the Retrieval-Augmented Generation (RAG) implementation, responsible for processing cybersecurity documents, generating embeddings, retrieving relevant information, and generating responses.

| File | Description |
|---|---|
| `__init__.py` | Marks the `rag` directory as a Python package and enables module imports. |
| `document_loader.py` | Loads and extracts content from PDF, TXT, DOCX, and CSV documents. |
| `text_chunker.py` | Splits extracted document content into smaller overlapping text chunks. |
| `embeddings.py` | Generates numerical vector representations (embeddings) of text chunks. |
| `vector_store.py` | Manages vector storage and database operations using ChromaDB. |
| `retriever.py` | Retrieves relevant document chunks based on user queries. |
| `generator.py` | Generates responses using the retrieved context and local language model. |

**Document Loader (`document_loader.py`)**

- Supports PDF, TXT, DOCX, and CSV file formats.
- Extracts text content from supported documents.
- Converts extracted content into a standard document structure containing:
  - `content`: Extracted text.
  - `metadata`: Original document information, such as filename, file type, and source path.
- Preserves page numbers for PDF documents and row numbers for CSV documents.
- Handles unsupported file formats and document extraction errors.

**Text Chunker (`text_chunker.py`)**

- Splits extracted document content into smaller text chunks for RAG processing.
- Uses a default chunk size of 800 characters.
- Uses a default overlap of 150 characters to preserve context between consecutive chunks.
- Preserves the original document metadata.
- Adds additional metadata to each chunk:
  - `chunk_index`: Position of the chunk.
  - `chunk_start`: Starting character offset.
  - `chunk_end`: Ending character offset.
- Supports processing individual documents and multiple documents.

#### 3.3 `security/`

Contains security mechanisms designed to protect application inputs, outputs, data, and interactions.

- **`input_validation.py`** – Validates user inputs before further processing.
- **`output_validation.py`** – Checks generated outputs before displaying responses to users.

#### 3.4 `config/`

Stores application configuration settings, such as model configurations, file paths, and system parameters.

- **`settings.py`** – Manages application settings and configuration values.

#### 3.5 `main.py`

Serves as the main application entry point and coordinates the execution of application components.

### 4. `storage/`

Stores local application data and generated resources required during runtime.

This includes the ChromaDB vector database, document metadata, and other persistent data generated by the application.

### 5. `tests/`

Contains unit tests used to verify individual components and overall system functionality.

| Test File | Description |
|---|---|
| `test_document_loader.py` | Tests document loading, text extraction, metadata handling, and unsupported file formats. |
| `test_text_chunker.py` | Tests text chunking, chunk size, overlap, metadata preservation, and invalid configurations. |
| `test_embeddings.py` | Tests embedding generation functionality. |
| `test_retrieval.py` | Tests document retrieval functionality. |

**Document Loader Unit Tests (`test_document_loader.py`)**

- Verifies TXT, DOCX, and CSV extraction.
- Tests unsupported file format handling.
- Verifies that the knowledge-base loader can process documents successfully.
- Ensures the expected document content and metadata are returned.

**Text Chunker Unit Tests (`test_text_chunker.py`)**

- Verifies empty and short text handling.
- Checks chunk size and overlap behaviour.
- Tests metadata preservation.
- Verifies multiple-document processing.
- Tests invalid chunk size and overlap configurations.

### 6. `.env.example`

Provides an example of environment variables required for configuring the application.

It serves as a template for developers to create their own local `.env` configuration file.

### 7. `.gitignore`

Specifies files and directories that Git should exclude from version control.

Examples include Python virtual environments, temporary files, environment variables, application logs, and locally generated database files.

### 8. `requirements.txt`

Lists the Python packages and dependencies required to install and run the project.

### 9. `README.md`

Provides an overview of the project, including its objectives, architecture, directory structure, setup instructions, technologies used, and development guidelines.

### 10. RAG Document Processing Workflow

The RAG document processing workflow consists of the following steps:

1. **Document Loading** – Load cybersecurity documents from the knowledge base.
2. **Text Extraction** – Extract text content and relevant metadata from supported file formats.
3. **Text Chunking** – Split extracted content into smaller chunks with overlapping text.
4. **Embedding Generation** – Convert text chunks into numerical vector representations.
5. **Vector Storage** – Store embeddings and associated metadata in ChromaDB.
6. **Document Retrieval** – Retrieve relevant chunks based on user queries.
7. **Response Generation** – Generate responses using the retrieved context and local language model.

### RAG Module Implementation Status

| Component | File | Status |
|---|---|---|
| Document Loading | `document_loader.py` | Completed |
| Text Chunking | `text_chunker.py` | Completed |
| Embedding Generation | `embeddings.py` | Planned |
| Vector Storage | `vector_store.py` | Planned |
| Document Retrieval | `retriever.py` | Planned |
| Response Generation | `generator.py` | Planned |
