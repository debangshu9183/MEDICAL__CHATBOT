#MEDICAL_CHATBOT — AI-Powered Medical Assistant
A fully functional Medical AI Chatbot built using:
* Groq LLaMA 3.1 / 70B (ultra-fast inference)
* AstraDB Vector Store (DataStax)
* LangChain RAG Pipeline
* Flask Web App
* Custom chat memory
* PDF/Data ingestion + embeddings
This project allows users to ask medical-related questions, and the bot replies using real context from your medical dataset. Deployed on AWS EC2 with nohup for persistent background running.
🚀 Features
✅ 1. RAG Pipeline (Retrieval-Augmented Generation)
* Embeds medical data (PDFs, text files)
* Stores embeddings in Astra DB vector database
* Retrieves relevant context for every question
✅ 2. Ultra-Fast LLM using GROQ
* Uses llama3-70b
* Very low latency
* Accurate medical reasoning
✅ 3. Flask Frontend Chat Interface
* Clean UI
* Live messaging
* User → Bot chat flow with timestamps
✅ 4. Persistent Chat Memory
* Remembers last few user/bot messages
* Better conversational flow
✅ 5. AWS Deployment (EC2)
* Host your Flask app publicly
* Run with nohup so it stays live even if you close your laptop
🗂 Project Structure

MEDICAL_CHATBOT/
│
├── app.py                 # Flask server
├── load.py                # Data ingestion runner (optional)
├── requirements.txt       # All dependencies
│
├── MEDIBOT/
│   ├── ingest.py          # Embedding + AstraDB vector store setup
│   ├── retrieval_generation.py  # RAG chain + Groq LLM
│   ├── data_converter.py  # Load medical PDFs/text
│   └── __init__.py
│
├── static/
│   └── style.css          # Chat UI design
│
├── templates/
│   └── chat.html          # Frontend HTML template
│
└── README.md              # Project documentation
🔧 Installation
1. Clone the Repository

git clone https://github.com/debangshu9183/MEDICAL_CHATBOT
cd MEDICAL_CHATBOT
🧩 Environment Variables
Create a .env file:

GROQ_API_KEY=your_groq_key_here
ASTRA_DB_API_ENDPOINT=https://xxxxxx.apps.astra.datastax.com
ASTRA_DB_APPLICATION_TOKEN=AstraCS:xxxxxx
ASTRA_DB_KEYSPACE=default_keyspace
📦 Install Dependencies
For local machine / EC2:

pip install -r requirements.txt
📥 Data Ingestion (Embedding Creation)
Runs once to load medical documents into AstraDB.

python3 MEDIBOT/ingest.py
Output:

Data conversion completed.
Number of documents: 6973
🤖 Start the Chatbot (Development Mode)

python3 app.py --host 0.0.0.0
Visit:

http://localhost:5000/
🌐 Deploy on AWS EC2 (Persistent Running)
Start app in background using nohup:

nohup python3 app.py --host 0.0.0.0 > app.log 2>&1 &
Check logs:

tail -f app.log
Stop the app:

pkill -f app.py
🧠 How the RAG System Works
1. User asks a medical question
2. Query → AstraDB vector store
3. Top-k relevant documents retrieved
4. System prompt + context passed to Groq LLM
5. Response generated safely with medical constraints
6. Memory stores last 3 user/bot messages
✨ Prompt Template

You are a professional medical assistant.
Use the retrieved medical context strictly.
If unsure, reply: “I don't know.”
Be concise, safe, and factual.
Never invent medical info.
🎨 Frontend Screenshot
Chat UI built using Bootstrap + custom CSS Clean, minimal medical theme.
📘 Future Enhancements
* Add user authentication
* Add voice chat (speech-to-text + text-to-speech)
* Add patient report upload
* Add dosage safety checks
🤝 Contributing
Pull requests are welcome! To contribute:

git checkout -b feature-branch
git commit -m "New feature"
git push origin feature-branch
📩 Contact
Developer: Debangshu Sadhukhan Email: debangshu.data@gmail.com GitHub: https://github.com/debangshu9183
⭐ If you like this project, don't forget to star the repository! make a detail professional redme\

Show more
🏥 MEDICAL CHATBOT — AI-Powered Medical Assistant
Show Image
Show Image
Show Image
Show Image

A production-ready Medical AI Chatbot leveraging cutting-edge Retrieval-Augmented Generation (RAG) technology to provide accurate, context-aware medical information. Built with Groq's ultra-fast LLaMA 3.1 70B model, AstraDB vector storage, and a responsive Flask web interface.

📋 Table of Contents
Overview
Key Features
Architecture
Technology Stack
Project Structure
Prerequisites
Installation
Configuration
Usage
Deployment
API Documentation
RAG Pipeline Details
Security & Best Practices
Performance Optimization
Troubleshooting
Future Roadmap
Contributing
License
Contact
🌟 Overview
MEDICAL_CHATBOT is an intelligent conversational assistant designed to answer medical queries using a sophisticated RAG (Retrieval-Augmented Generation) pipeline. The system combines vector-based document retrieval with large language model reasoning to provide accurate, contextually relevant medical information while maintaining strict safety protocols.

Why This Project?
Accuracy First: Uses actual medical documentation rather than hallucinating information
Lightning Fast: Groq infrastructure provides sub-second response times
Scalable: Vector database architecture supports millions of document chunks
Production Ready: Deployed on AWS EC2 with persistent background processing
Memory-Aware: Maintains conversation context for natural dialogue flow
✨ Key Features
🔍 Advanced RAG Pipeline
Intelligent Document Retrieval: Semantic search across embedded medical documents
Vector Storage: Powered by DataStax AstraDB for distributed, scalable storage
Context-Aware Responses: Top-k retrieval ensures relevant information backing every answer
Embeddings: High-quality vector representations using state-of-the-art embedding models
🚀 Ultra-Fast Inference
Groq LLaMA 3.1 70B: Industry-leading inference speed (hundreds of tokens/second)
Low Latency: Sub-second response times for real-time conversations
High Throughput: Handles multiple concurrent users efficiently
💬 Conversational Interface
Clean Web UI: Responsive Bootstrap-based design
Real-Time Chat: Seamless message flow with typing indicators
Message History: Persistent chat memory for context retention
Timestamps: Track conversation timeline
🔒 Safety-First Design
Constrained Responses: System prompts enforce medical safety protocols
Uncertainty Handling: Bot explicitly states when information is unavailable
Source Verification: Responses grounded in retrieved documents
No Hallucination: Strict prompt engineering prevents fabricated medical advice
☁️ Cloud Deployment
AWS EC2 Hosting: Publicly accessible endpoint
Background Processing: nohup ensures 24/7 availability
Logging: Comprehensive application logs for monitoring
Scalability: Easy horizontal scaling with load balancers
🏗 Architecture
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface (Flask)                   │
│                     templates/chat.html + CSS                    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Flask Application Layer                     │
│                          (app.py)                                │
│    • Route handling                                              │
│    • Session management                                          │
│    • Chat memory orchestration                                   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   RAG Pipeline (retrieval_generation.py)         │
│                                                                   │
│   ┌─────────────────┐         ┌──────────────────┐              │
│   │  Query Embedding │────────▶│ Vector Search    │              │
│   │  Processing      │         │ (AstraDB)        │              │
│   └─────────────────┘         └──────────────────┘              │
│                                         │                         │
│                                         ▼                         │
│                             ┌──────────────────────┐             │
│                             │ Top-K Document       │             │
│                             │ Retrieval            │             │
│                             └──────────────────────┘             │
│                                         │                         │
│                                         ▼                         │
│   ┌─────────────────────────────────────────────────────┐       │
│   │        Context + Query → Groq LLaMA 3.1 70B         │       │
│   │        (llama3-70b-8192 via Groq API)               │       │
│   └─────────────────────────────────────────────────────┘       │
│                                         │                         │
│                                         ▼                         │
│                             ┌──────────────────────┐             │
│                             │ Generated Response   │             │
│                             └──────────────────────┘             │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Ingestion Pipeline                       │
│                                                                   │
│   PDF/Text Files ────▶ data_converter.py ────▶ Chunks           │
│                              │                                    │
│                              ▼                                    │
│                        Embedding Model                            │
│                              │                                    │
│                              ▼                                    │
│                    AstraDB Vector Store                           │
│                       (ingest.py)                                 │
└─────────────────────────────────────────────────────────────────┘
Data Flow
Ingestion Phase (One-time setup):
Medical documents (PDFs, text) → Parsed and chunked
Chunks → Embedded using embedding model
Embeddings → Stored in AstraDB with metadata
Query Phase (Real-time):
User question → Embedded using same model
Vector similarity search → Top-k relevant chunks retrieved
Retrieved context + conversation history + system prompt → Groq LLM
Generated response → Returned to user
Conversation stored in chat memory
🛠 Technology Stack
Component	Technology	Purpose
LLM	Groq LLaMA 3.1 70B	Ultra-fast inference for response generation
Vector Database	DataStax AstraDB	Distributed storage for document embeddings
Orchestration	LangChain	RAG pipeline management and LLM chains
Web Framework	Flask 2.0+	Backend API and server
Frontend	HTML5, CSS3, Bootstrap 5	Responsive chat interface
Embeddings	Sentence Transformers / OpenAI	Document and query vectorization
Cloud Platform	AWS EC2	Application hosting
Process Management	nohup	Background process persistence
Environment	Python 3.8+	Runtime environment
📁 Project Structure
MEDICAL_CHATBOT/
│
├── app.py                          # Main Flask application entry point
├── load.py                         # Optional data loading utility
├── requirements.txt                # Python dependencies
├── .env                            # Environment variables (not in repo)
├── .gitignore                      # Git ignore rules
├── README.md                       # Project documentation
├── LICENSE                         # License file
│
├── MEDIBOT/                        # Core application package
│   ├── __init__.py                 # Package initializer
│   ├── ingest.py                   # Data ingestion and embedding pipeline
│   ├── retrieval_generation.py    # RAG chain implementation
│   ├── data_converter.py          # Document parsing and chunking
│   └── prompts.py                  # System prompt templates (optional)
│
├── data/                           # Medical documents directory
│   ├── pdfs/                       # PDF medical resources
│   └── text/                       # Text-based medical data
│
├── static/                         # Static web assets
│   ├── css/
│   │   └── style.css               # Custom styling
│   ├── js/
│   │   └── chat.js                 # Frontend JavaScript (optional)
│   └── images/
│       └── logo.png                # Application logo
│
├── templates/                      # Jinja2 HTML templates
│   ├── chat.html                   # Main chat interface
│   └── base.html                   # Base template (optional)
│
├── logs/                           # Application logs
│   └── app.log                     # Runtime logs
│
└── tests/                          # Unit tests
    ├── test_ingest.py
    ├── test_rag.py
    └── test_api.py
📋 Prerequisites
System Requirements
OS: Linux (Ubuntu 20.04+ recommended), macOS, or Windows with WSL
Python: 3.8 or higher
RAM: Minimum 4GB (8GB recommended)
Storage: 10GB free space for documents and embeddings
Required Accounts
Groq Account: Sign up at Groq
Obtain API key from console
DataStax Astra Account: Create account
Create a vector-enabled database
Generate application token
AWS Account (for deployment): AWS Console
🚀 Installation
1. Clone the Repository
bash
git clone https://github.com/debangshu9183/MEDICAL_CHATBOT.git
cd MEDICAL_CHATBOT
2. Create Virtual Environment
bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
bash
pip install --upgrade pip
pip install -r requirements.txt
4. Verify Installation
bash
python -c "import langchain; import flask; print('Installation successful!')"
⚙️ Configuration
Environment Variables
Create a .env file in the project root:

env
# Groq API Configuration
GROQ_API_KEY=gsk_your_groq_api_key_here

# AstraDB Configuration
ASTRA_DB_API_ENDPOINT=https://your-database-id.apps.astra.datastax.com
ASTRA_DB_APPLICATION_TOKEN=AstraCS:your_token_here
ASTRA_DB_KEYSPACE=default_keyspace

# Optional: Embedding Model Configuration
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your_secret_key_for_sessions

# Application Settings
MAX_CHAT_HISTORY=5
TOP_K_DOCUMENTS=3
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
AstraDB Setup
Create Database:
Login to Astra Console
Create new database with Vector Search enabled
Note your Database ID and Region
Generate Token:
Navigate to Settings → Application Tokens
Create token with appropriate permissions
Copy token securely
Create Keyspace (if not using default):
sql
   CREATE KEYSPACE medical_data WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
📖 Usage
Data Ingestion (One-Time Setup)
Before first use, ingest your medical documents into the vector database:

bash
# Place your medical PDFs/text files in the data/ directory
python3 MEDIBOT/ingest.py
```

**Expected Output**:
```
Starting data conversion...
Processing: medical_handbook.pdf
Processing: drug_database.txt
...
Data conversion completed.
Number of documents: 6973
Creating embeddings...
Embeddings created successfully.
Storing in AstraDB...
✓ Data ingestion complete!
Running the Application
Development Mode
bash
python3 app.py
Access at: http://localhost:5000

Production Mode (Specify Host/Port)
bash
python3 app.py --host 0.0.0.0 --port 8080
Using the Chatbot
Open the web interface in your browser
Type your medical question in the input field
Press Enter or click Send
Receive AI-generated response based on your medical documents
Continue the conversation - the bot remembers context
Example Queries:
"What are the symptoms of Type 2 diabetes?"
"Explain the mechanism of action for metformin"
"What are contraindications for aspirin use?"
"Describe the treatment protocol for hypertension"
☁️ Deployment
AWS EC2 Deployment
1. Launch EC2 Instance
bash
# Recommended: Ubuntu 22.04 LTS, t2.medium or larger
# Security Group: Allow inbound on port 5000 (or your chosen port)
2. Connect to Instance
bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
3. Install Dependencies
bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
4. Clone and Setup
bash
git clone https://github.com/debangshu9183/MEDICAL_CHATBOT.git
cd MEDICAL_CHATBOT
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
5. Configure Environment
bash
nano .env
# Paste your environment variables
# Save with Ctrl+X, Y, Enter
6. Run Ingestion (if needed)
bash
python3 MEDIBOT/ingest.py
7. Start Application with nohup
bash
nohup python3 app.py --host 0.0.0.0 --port 5000 > logs/app.log 2>&1 &
8. Verify Running
bash
# Check process
ps aux | grep app.py

# Monitor logs
tail -f logs/app.log

# Test endpoint
curl http://localhost:5000
9. Access Publicly
Open your browser to: http://your-ec2-public-ip:5000

Process Management
bash
# Stop the application
pkill -f app.py

# Restart
nohup python3 app.py --host 0.0.0.0 --port 5000 > logs/app.log 2>&1 &

# Check status
ps aux | grep app.py
Using systemd (Recommended for Production)
Create a systemd service file:

bash
sudo nano /etc/systemd/system/medical-chatbot.service
ini
[Unit]
Description=Medical Chatbot Flask Application
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/MEDICAL_CHATBOT
Environment="PATH=/home/ubuntu/MEDICAL_CHATBOT/venv/bin"
ExecStart=/home/ubuntu/MEDICAL_CHATBOT/venv/bin/python3 app.py --host 0.0.0.0 --port 5000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
Enable and start:

bash
sudo systemctl daemon-reload
sudo systemctl enable medical-chatbot
sudo systemctl start medical-chatbot
sudo systemctl status medical-chatbot
📡 API Documentation
POST /chat
Send a message to the chatbot and receive a response.

Request:

json
{
  "message": "What are the symptoms of diabetes?"
}
Response:

json
{
  "response": "Based on the medical literature, common symptoms of diabetes include...",
  "timestamp": "2025-11-14T10:30:00Z",
  "sources": [
    {
      "document": "diabetes_handbook.pdf",
      "page": 12
    }
  ]
}
Status Codes:

200 OK: Successful response
400 Bad Request: Missing or invalid message
500 Internal Server Error: Server-side error
🔍 RAG Pipeline Details
Document Processing
Loading: PDFs and text files parsed using LangChain loaders
Chunking: Documents split into manageable chunks
Default size: 1000 characters
Overlap: 200 characters (ensures context continuity)
Metadata: Each chunk tagged with source, page number, timestamp
Embedding Generation
python
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
Vector Storage
Database: AstraDB (Cassandra-based)
Similarity Metric: Cosine similarity
Index: Approximate Nearest Neighbor (ANN) for fast retrieval
Retrieval Strategy
python
# Top-k retrieval with score threshold
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 3,
        "score_threshold": 0.7
    }
)
Prompt Engineering
python
system_prompt = """
You are a professional medical assistant with access to verified medical literature.

Guidelines:
1. Use ONLY the provided context to answer questions
2. If information is not in the context, respond: "I don't have enough information to answer that safely."
3. Be concise and factual
4. Never fabricate medical information
5. Include source citations when possible
6. For serious conditions, recommend consulting a healthcare professional

Context:
{context}

Conversation History:
{chat_history}

Question: {question}

Answer:"""
Response Generation
python
from langchain.chains import ConversationalRetrievalChain

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=groq_llm,
    retriever=retriever,
    memory=chat_memory,
    return_source_documents=True
)
🔒 Security & Best Practices
Environment Variables
✅ Never commit .env files to version control
✅ Use strong, unique tokens for all services
✅ Rotate API keys regularly
Input Validation
python
def sanitize_input(user_message):
    # Remove potentially harmful characters
    # Limit message length
    # Validate encoding
    return cleaned_message
Rate Limiting
python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    default_limits=["200 per day", "50 per hour"]
)
```

### HTTPS Enforcement
- Use reverse proxy (Nginx) with SSL certificates
- Redirect HTTP to HTTPS

### Medical Disclaimer
Always include a disclaimer:
```
⚠️ This chatbot provides information for educational purposes only. 
It is not a substitute for professional medical advice, diagnosis, or treatment. 
Always consult a qualified healthcare provider for medical concerns.
⚡ Performance Optimization
Caching
python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_embedding(text):
    return embedding_model.embed_query(text)
Async Processing
python
import asyncio

async def process_query(query):
    # Parallel retrieval and embedding
    results = await asyncio.gather(
        retrieve_documents(query),
        generate_embedding(query)
    )
    return results
Database Connection Pooling
AstraDB automatically handles connection pooling
Configure max connections in client settings
Monitoring
python
import logging

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
🐛 Troubleshooting
Common Issues
1. "AstraDB Connection Failed"
bash
# Verify credentials
echo $ASTRA_DB_API_ENDPOINT
echo $ASTRA_DB_APPLICATION_TOKEN

# Test connection
python3 -c "from astrapy import DataAPIClient; client = DataAPIClient('your_token'); print('Connected!')"
2. "Groq API Rate Limit Exceeded"
Check your Groq console for usage limits
Implement exponential backoff
Upgrade to higher tier plan
3. "Slow Response Times"
Reduce top_k value
Optimize chunk size
Enable caching
Check EC2 instance type (upgrade if needed)
4. "Out of Memory"
Batch document processing
Increase EC2 instance RAM
Reduce concurrent users
Debug Mode
bash
FLASK_ENV=development FLASK_DEBUG=True python3 app.py
Logs Analysis
bash
# View recent errors
grep ERROR logs/app.log | tail -20

# Monitor in real-time
tail -f logs/app.log
🗺 Future Roadmap
Phase 1: Enhanced Security
 User authentication (OAuth 2.0)
 Role-based access control
 Audit logging
 HIPAA compliance features
Phase 2: Advanced Features
 Voice input (Speech-to-Text)
 Voice output (Text-to-Speech)
 Multi-language support
 Medical image analysis integration
Phase 3: Clinical Integration
 Patient report upload and analysis
 Lab result interpretation
 Drug interaction checker
 Dosage calculator
Phase 4: Scalability
 Kubernetes deployment
 Load balancing
 Auto-scaling
 Multi-region deployment
Phase 5: Intelligence
 Fine-tuned medical models
 Symptom checker
 Diagnosis suggestion system
 Treatment recommendation engine
🤝 Contributing
We welcome contributions! Please follow these steps:

1. Fork the Repository
bash
# Click "Fork" on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/MEDICAL_CHATBOT.git
cd MEDICAL_CHATBOT
2. Create a Feature Branch
bash
git checkout -b feature/your-feature-name
3. Make Changes
Write clean, documented code
Follow PEP 8 style guidelines
Add unit tests for new features
4. Test Your Changes
bash
# Run tests
pytest tests/

# Check code style
flake8 MEDIBOT/ app.py

# Format code
black MEDIBOT/ app.py
5. Commit and Push
bash
git add .
git commit -m "feat: Add voice input support"
git push origin feature/your-feature-name
```

### 6. Create Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Provide detailed description of changes
- Reference any related issues

### Contribution Guidelines

- **Code Quality**: Maintain high standards
- **Documentation**: Update README for new features
- **Tests**: Ensure 80%+ code coverage
- **Commit Messages**: Use conventional commits format
  - `feat:` New feature
  - `fix:` Bug fix
  - `docs:` Documentation changes
  - `refactor:` Code refactoring
  - `test:` Test additions

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
```
MIT License

Copyright (c) 2025 Debangshu Sadhukhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
📞 Contact
Developer
Debangshu Sadhukhan

📧 Email: debangshu.data@gmail.com
🐙 GitHub: @debangshu9183
