# VULNIX - Local AI Vulnerability Management Assistant

An AI-powered vulnerability analysis and prioritization system that helps security analysts identify high-risk vulnerabilities, understand their potential impact, and determine appropriate remediation actions.

## Three Main Pillars

| Pillar | Description |
|---|---|
| **Prioritize** | Identify critical risks and determine which vulnerabilities require attention first. |
| **Analyze** | Understand vulnerability details, severity, affected products, and potential impact. |
| **Remediate** | Retrieve remediation guidance and recommend appropriate fixes or mitigation actions. |

---

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

---

# Project Directory Structure

The project is organised into several directories to separate vulnerability knowledge resources, application components, RAG implementation, security mechanisms, local storage, and testing files.

## Overall Directory Structure

```text
local-ai-soc/
│
├── knowledge_base/
│   ├── vulnerability_data/
│   │   ├── nvd/
│   │   └── cisa_kev/
│   │
│   ├── vulnerability_analysis/
│   │   ├── cvss/
│   │   └── cwe/
│   │
│   ├── risk_prioritization/
│   │
│   ├── remediation_guidance/
│   │   ├── vendor_advisories/
│   │   └── mitigation_guidelines/
│   │
│   └── reference_documents/
│       ├── nist/
│       └── cis/
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

## 1. `knowledge_base/`

Stores cybersecurity vulnerability resources and reference documents used by the Retrieval-Augmented Generation (RAG) system.

The knowledge base is organised according to the project's three main pillars: Prioritize, Analyze, and Remediate.

### 1.1 `vulnerability_data/`

Stores vulnerability records and structured vulnerability information from recognised cybersecurity sources.

| Folder | Description |
|---|---|
| `nvd/` | Stores vulnerability information from the National Vulnerability Database (NVD), including CVE descriptions, affected configurations, and available severity data. |
| `cisa_kev/` | Stores the CISA Known Exploited Vulnerabilities (KEV) Catalog, which identifies vulnerabilities known to have been exploited in the wild. |

**Purpose:**
- Provides the primary vulnerability information used by the system.
- Supports CVE identification and vulnerability information retrieval.
- Supplies vulnerability records for further analysis and prioritization.

### 1.2 `vulnerability_analysis/`

Stores resources used to understand and analyse vulnerability characteristics, severity, and potential impact.

| Folder | Description |
|---|---|
| `cvss/` | Stores Common Vulnerability Scoring System (CVSS) information, scoring guidelines, and related reference materials. |
| `cwe/` | Stores Common Weakness Enumeration (CWE) information, including software and hardware weakness classifications. |

**Purpose:**
- Supports vulnerability severity analysis.
- Helps explain vulnerability characteristics and underlying weaknesses.
- Provides reference information for understanding potential vulnerability impact.

### 1.3 `risk_prioritization/`

Stores resources and guidelines used to assess and prioritise vulnerabilities according to their risk factors.

**Purpose:**
- Supports vulnerability prioritization.
- Provides reference materials for evaluating exploitation status and other relevant risk factors.
- Helps identify vulnerabilities that may require more urgent attention.

Risk prioritization should consider multiple factors. CVSS severity alone does not represent an organisation's complete business risk.

### 1.4 `remediation_guidance/`

Stores vendor security advisories, remediation instructions, patches, and mitigation recommendations.

| Folder | Description |
|---|---|
| `vendor_advisories/` | Stores security advisories and vulnerability remediation information from vendors such as Microsoft, Cisco, and Fortinet. |
| `mitigation_guidelines/` | Stores mitigation procedures, workaround instructions, and security recommendations for addressing vulnerabilities. |

**Purpose:**
- Provides vendor-specific remediation information.
- Helps identify available patches and fixes.
- Supports the generation of evidence-based remediation recommendations.

### 1.5 `reference_documents/`

Stores general cybersecurity standards, frameworks, and reference documents that support vulnerability management.

| Folder | Description |
|---|---|
| `nist/` | Stores relevant National Institute of Standards and Technology (NIST) publications and vulnerability management guidance. |
| `cis/` | Stores relevant Center for Internet Security (CIS) guidelines and security recommendations. |

**Purpose:**
- Provides additional reference materials for vulnerability management.
- Supports risk assessment and remediation practices.
- Supplies security guidance that can be referenced across the three main project pillars.

---

## 2. `logs/`

Stores application and system log files generated during development and execution.

These logs help developers:
- Troubleshoot application errors.
- Monitor application activities.
- Investigate unexpected behaviour.
- Review relevant system events.

## 3. `src/`

Contains the main source code of the Local AI Vulnerability Management Assistant.

### 3.1 `app/`

Contains the application interface and user interaction components.

- **`streamlit_app.py`** – Provides the Streamlit-based user interface for interacting with the Local AI Vulnerability Management Assistant.

### 3.2 `rag/`

Contains the Retrieval-Augmented Generation (RAG) implementation, responsible for processing vulnerability documents, generating embeddings, retrieving relevant information, and generating responses using the local language model.

| File | Description |
|---|---|
| `__init__.py` | Marks the `rag` directory as a Python package and enables module imports. |
| `document_loader.py` | Loads and extracts content from PDF, TXT, DOCX, and CSV documents. |
| `text_chunker.py` | Splits extracted document content into smaller overlapping text chunks. |
| `embeddings.py` | Generates numerical vector representations (embeddings) of text chunks. |
| `vector_store.py` | Manages vector storage and database operations using ChromaDB. |
| `retriever.py` | Retrieves relevant document chunks based on user queries. |
| `generator.py` | Generates responses using retrieved context and the local language model. |

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

### 3.3 `security/`

Contains security mechanisms designed to protect application inputs, outputs, data, and interactions.

- **`input_validation.py`** – Validates user inputs before further processing.
- **`output_validation.py`** – Checks generated outputs before displaying responses to users.

### 3.4 `config/`

Stores application configuration settings, such as model configurations, file paths, and system parameters.

- **`settings.py`** – Manages application settings and configuration values.

### 3.5 `main.py`

Serves as the main application entry point and coordinates the execution of application components.

---

## 4. `storage/`

Stores local application data and generated resources required during runtime.

This may include:
- ChromaDB vector database files.
- Indexed document data.
- Document metadata.
- Other persistent data generated by the application.

## 5. `tests/`

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

---

## 6. `.env.example`

Provides an example of environment variables required for configuring the application.

It serves as a template for developers to create their own local `.env` configuration file.

## 7. `.gitignore`

Specifies files and directories that Git should exclude from version control.

Examples include:
- Python virtual environments.
- Temporary and compiled Python files.
- Environment variables and secrets.
- Application logs.
- Locally generated database files.
- Other development-specific files.

## 8. `requirements.txt`

Lists the Python packages and dependencies required to install and run the project.

## 9. `README.md`

Provides an overview of the project, including its objectives, architecture, directory structure, setup instructions, technologies used, and development guidelines.

---

# 10. RAG Document Processing Workflow

The RAG document processing workflow consists of the following steps:

1. **Document Loading** – Load vulnerability records and reference documents from the knowledge base.
2. **Text Extraction** – Extract text content and relevant metadata from supported document formats.
3. **Text Chunking** – Split extracted content into smaller chunks with overlapping text.
4. **Embedding Generation** – Convert text chunks into numerical vector representations using the local embedding model.
5. **Vector Storage** – Store embeddings and associated metadata in ChromaDB.
6. **Document Retrieval** – Retrieve relevant information based on user queries.
7. **Response Generation** – Generate responses using the retrieved context and local language model.

**Note:** Structured vulnerability records, such as CVE JSON data, may require dedicated parsing and metadata extraction instead of being processed as ordinary text documents.

## 11. Knowledge Retrieval Across the Three Main Pillars

The RAG system can retrieve information from multiple knowledge-base categories to support different user requirements.

| Main Pillar | Relevant Knowledge Base Sources | Expected Function |
|---|---|---|
| **Prioritize** | `vulnerability_data/cisa_kev/`, `vulnerability_analysis/cvss/`, `risk_prioritization/` | Identify potentially critical vulnerabilities using exploitation information, severity, and other relevant risk factors. |
| **Analyze** | `vulnerability_data/nvd/`, `vulnerability_analysis/cvss/`, `vulnerability_analysis/cwe/`, `reference_documents/` | Retrieve and explain CVE details, severity information, affected products, and vulnerability characteristics. |
| **Remediate** | `remediation_guidance/vendor_advisories/`, `remediation_guidance/mitigation_guidelines/`, `reference_documents/` | Retrieve vendor fixes, patches, workarounds, and mitigation recommendations. |

A single source may support more than one pillar. For example, CVSS information can support both vulnerability analysis and risk prioritization.

The system should use document metadata to identify the source, category, CVE ID, document type, and update date. This allows the same information to be retrieved by different functions without duplicating files across the knowledge base.

---

# 12. RAG Module Implementation Status

| Component | File | Status |
|---|---|---|
| Document Loading | `document_loader.py` | Completed |
| Text Chunking | `text_chunker.py` | Completed |
| Embedding Generation | `embeddings.py` | Planned |
| Vector Storage | `vector_store.py` | Planned |
| Document Retrieval | `retriever.py` | Planned |
| Response Generation | `generator.py` | Planned |

**Implementation status should be updated whenever a component is implemented and tested.**