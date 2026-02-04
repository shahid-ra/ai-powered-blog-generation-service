# AI Powered Blog Generation Service

A FastAPI service that generates blog posts using AI-powered multi-agent orchestration. The service uses CrewAI to coordinate a research agent and a writer agent to produce well-researched, high-quality blog content.

## Features

- Multi-agent architecture using CrewAI
- Web research using DuckDuckGo search
- Four blog generation styles: Professional, Educational, Informational, Storytelling
- Returns source links used during research
- RESTful API with FastAPI

## Prerequisites

- Python 3.12+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-powered-blog-generation-service
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set your OpenAI API key in the config file:

**For development** (`app/configs/config_dev.yml`):
```yaml
application:
  version: 1.0.0
  name: AI Powered Blog Generation Service
  description: A service to generate blog content using AI.
  environment: dev

OPENAI_API_KEY: your-openai-api-key-here
```

**For production** (`app/configs/config_prod.yml`):
```yaml
OPENAI_API_KEY: ${OPENAI_API_KEY}
```
Set the environment variable: `export OPENAI_API_KEY=your-key`

2. Set the environment (optional, defaults to `dev`):
```bash
export ENVIRONMENT=dev  # or qa, prod
```

## Running the Application

Start the server:
```bash
source venv/bin/activate
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check
```
GET /v1/health/
```
Returns service health status.

### Generate Blog
```
POST /v1/blog/generate
```

**Request Body:**
```json
{
  "topic": "The Future of Artificial Intelligence",
  "generation_type": "professional"
}
```

**Generation Types:**
- `professional` - Authoritative, expert-focused content
- `educational` - Teaching with examples and explanations
- `informational` - Objective facts and insights
- `storytelling` - Narrative-driven, engaging content

**Response:**
```json
{
  "topic": "The Future of Artificial Intelligence",
  "generation_type": "professional",
  "content": "# The Future of Artificial Intelligence\n\n...",
  "sources": [
    {
      "title": "AI Research Article",
      "url": "https://example.com/ai-article"
    }
  ],
  "status": "success"
}
```

## Example Usage

Using curl:
```bash
curl -X POST http://localhost:8000/v1/blog/generate \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Benefits of Remote Work",
    "generation_type": "informational"
  }'
```

Using Python:
```python
import requests

response = requests.post(
    "http://localhost:8000/v1/blog/generate",
    json={
        "topic": "Benefits of Remote Work",
        "generation_type": "informational"
    }
)
print(response.json())
```

## API Documentation

Once the server is running, access the interactive API docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
app/
├── agents/
│   ├── research_agent.py    # Research agent with web search
│   └── writer_agent.py      # Writer agent for content generation
├── configs/
│   ├── config.py            # Configuration loader
│   ├── config_dev.yml       # Development config
│   ├── config_prod.yml      # Production config
│   └── config_qa.yml        # QA config
├── models/
│   ├── blog_generation_type.py  # Blog style enum
│   └── blog_request.py      # Request/Response models
├── orchestration/
│   ├── blog_crew.py         # CrewAI orchestration
│   └── tools/
│       └── search_tool.py   # Web search tool
├── routes/
│   ├── blog_api.py          # Blog generation endpoint
│   └── health_api.py        # Health check endpoint
├── search/
│   └── ddgs_wrapper.py      # DuckDuckGo search wrapper
└── main.py                  # FastAPI application entry point
```
