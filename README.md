# ElysiaAI: Your AI-Powered Mental Wellness Companion

ElysiaAI is an innovative AI-powered mental wellness companion designed to provide empathetic support and guidance. It acts as a conversational agent that can engage in therapeutic dialogue and, when appropriate, assist users in finding professional mental health resources.

## Features

- **Empathetic AI Chat**: Engage in supportive and therapeutic conversations powered by a specialized language model.
- **Intelligent Routing**: The AI intelligently determines whether to respond directly or to suggest external resources based on the conversation's context.
- **Therapist Locator**: Integrated web search functionality to help users find mental health professionals nearby.
- **User-Friendly Interface**: A simple and intuitive chat interface for seamless interaction.

## Architecture

ElysiaAI follows a client-server architecture:

-   **Frontend**: A web-based chat application built with Streamlit, providing the user interface for interaction with the AI.
-   **Backend**: A robust API service built with FastAPI, housing the core AI logic. This backend utilizes the LangChain framework to orchestrate interactions between various large language models and tools.

The AI agent within the backend operates as follows:
1.  **Primary Agent (Google Gemini)**: This agent acts as a router, analyzing user input.
2.  **Therapeutic LLM (MedGemma via Ollama)**: For therapeutic conversations, the primary agent routes queries to a locally run, specialized therapeutic language model (MedGemma) via Ollama.
3.  **Web Search Tool**: For queries related to finding therapists or external information, the primary agent utilizes a DuckDuckGo search tool.

## Technologies Used

### Frontend
-   **Streamlit**: For creating interactive web applications with Python.

### Backend
-   **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
-   **LangChain**: A framework for developing applications powered by language models.
-   **Google Gemini**: The primary large language model used for intelligent routing and general conversation.
-   **Ollama**: For running large language models locally, specifically hosting the MedGemma therapeutic model.
-   **MedGemma**: A specialized open-source therapeutic language model.
-   **DuckDuckGo Search**: Utilized for web searches to find external resources like therapists.

## Setup and Installation

Follow these steps to get ElysiaAI up and running on your local machine.

### Prerequisites

-   Python 3.9+
-   `uv` (a fast Python package installer and resolver, similar to `pip` and `pip-tools`)
-   Ollama (for running MedGemma locally)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ElysiaAI.git
cd ElysiaAI
```

### 2. Install Python Dependencies

ElysiaAI uses `uv` for dependency management.

```bash
uv sync
```

### 3. Set up Ollama and MedGemma

Download and install Ollama from [ollama.ai](https://ollama.ai/).

Once Ollama is installed, pull the `medgemma` model:

```bash
ollama pull medgemma
```

### 4. Configure Environment Variables

Create a `.env` file in the `backend` directory (e.g., `backend/.env`) and add your Google API key for Gemini:

```
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
```
Replace `"YOUR_GEMINI_API_KEY"` with your actual Google API key.

### 5. Run the Backend

Navigate to the `backend` directory and start the FastAPI server:

```bash
cd backend
python main.py
```
The backend will typically run on `http://127.0.0.1:8000`.

### 6. Run the Frontend

In a new terminal, navigate back to the root directory of the project and start the Streamlit application:

```bash
cd ..
streamlit run frontend.py
```

This will open the ElysiaAI chat interface in your web browser, usually at `http://localhost:8501`.

## Usage

-   Open your web browser to the address provided by Streamlit (e.g., `http://localhost:8501`).
-   Type your messages into the chat input box and press Enter or click the send button.
-   The AI will respond based on your input, offering therapeutic support or directing you to relevant resources.

## Contributing

We welcome contributions to ElysiaAI! Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
