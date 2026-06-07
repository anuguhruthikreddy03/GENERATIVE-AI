# 📝 Blog Assistant Chatbot

An AI-powered Blog Assistant Chatbot built using **Streamlit**, **LangChain**, and **Google Gemini 2.5 Flash Lite**. This chatbot helps content creators, bloggers, marketers, and writers generate high-quality blog content, improve existing articles, create SEO-friendly titles, and enhance overall writing quality.

---

## 🚀 Features

### ✍️ Blog Content Generation
Generate complete blog articles on any topic with well-structured content.

### 🔍 SEO-Friendly Title Generation
Create engaging and search-engine-optimized blog titles.

### 📄 Blog Summarization
Summarize long articles into concise and readable content.

### ✨ Content Rewriting
Rewrite blog content in a professional, clear, and engaging manner.

### 📝 Grammar & Readability Improvement
Improve sentence structure, grammar, clarity, and overall readability.

### 📈 SEO Keyword Suggestions
Generate relevant SEO keywords to improve content visibility.

### #️⃣ Hashtag Recommendations
Suggest hashtags for social media promotion and content marketing.

### 💬 Interactive Chat Interface
User-friendly chat interface built with Streamlit's chat components.

---

# 🏗️ Project Architecture

```text
User Input
     │
     ▼
Streamlit Chat Interface
     │
     ▼
LangChain
     │
     ▼
Google Gemini 2.5 Flash Lite
     │
     ▼
Generated Response
     │
     ▼
Displayed in Chat Window
```

---

# 📂 Project Structure

```text
chatbot/
│
├── app.py
├── code.py
├── .env
├── chatbot.log
└── README.md
```

### File Description

| File | Purpose |
|--------|---------|
| app.py | Streamlit frontend application |
| code.py | Gemini API integration and response generation |
| .env | Stores API keys securely |
| chatbot.log | Application logs |
| README.md | Project documentation |

---

# 🛠️ Technologies Used

### Frontend

- Streamlit

### Backend

- Python

### AI Framework

- LangChain

### Large Language Model

- Gemini 2.5 Flash Lite

### Environment Management

- Python Dotenv

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install streamlit
pip install langchain
pip install langchain-google-genai
pip install python-dotenv
```

Or install all requirements using:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
API_KEY=YOUR_GEMINI_API_KEY
```

Replace:

```text
YOUR_GEMINI_API_KEY
```

with your actual Google Gemini API key.

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After execution, Streamlit will provide a local URL:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 💡 Example Prompts

### Blog Generation

```text
Write a blog on Artificial Intelligence in Healthcare.
```

### SEO Title Generation

```text
Generate 10 SEO-friendly titles for a blog about Machine Learning.
```

### Blog Summary

```text
Summarize the following blog article.
```

### Content Rewriting

```text
Rewrite this article in a professional tone.
```

### SEO Keywords

```text
Suggest SEO keywords for a blog about Generative AI.
```

### Hashtag Suggestions

```text
Generate hashtags for a blog about Data Science.
```

---

# 🔄 Application Workflow

### Step 1

User enters a query through the Streamlit chat interface.

### Step 2

The query is sent to the response generation module.

### Step 3

A predefined system prompt guides the AI assistant's behavior.

### Step 4

LangChain sends the request to the Gemini model.

### Step 5

Gemini generates a response based on the user query.

### Step 6

The generated response is displayed in the chat window.

### Step 7

Chat history is maintained using Streamlit Session State.

---

# 🎯 Use Cases

- Blog Writing
- Content Marketing
- SEO Optimization
- Academic Writing Assistance
- Article Summarization
- Social Media Content Creation
- Technical Documentation
- Content Enhancement

---

# 🔒 Security Considerations

- Store API keys in environment variables.
- Never hardcode API credentials in source code.
- Add `.env` to `.gitignore` before pushing to GitHub.

Example:

```gitignore
.env
__pycache__/
venv/
```

# 🎓 Learning Outcomes

This project demonstrates:

- Streamlit Application Development
- LangChain Integration
- Google Gemini API Usage
- Prompt Engineering
- Environment Variable Management
- Conversational AI Development
- LLM-Powered Content Generation

---

# 📌 Conclusion

The Blog Assistant Chatbot is a lightweight Generative AI application that combines Streamlit, LangChain, and Gemini to help users create, improve, summarize, and optimize blog content. It provides an intuitive chat interface and demonstrates how Large Language Models can be integrated into real-world content creation workflows.
