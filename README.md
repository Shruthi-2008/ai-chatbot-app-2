# 🤖 AI Chatbot Assistant

A conversational AI chatbot built with a **FastAPI** backend and a **Streamlit** frontend. This application leverages **Llama 3.2** to provide intelligent responses in a clean, user-friendly interface.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-009688)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)

## 🚀 Features

* **Interactive UI:** Clean chat interface built with Streamlit.
* **High Performance Backend:** Asynchronous API handling using FastAPI.
* **LLM Integration:** Powered by **Llama 3.2** for natural language understanding.
* **Session History:** Maintains context within the chat session.
* **Modular Design:** Clean separation between frontend logic and backend services.

## 🛠️ Tech Stack

* **Language:** Python
* **Backend:** FastAPI, Uvicorn
* **Frontend:** Streamlit
* **AI Model:** Llama 3.2
* **Version Control:** GitHub

---

## 📂 Project Structure

```bash
ai-chatbot/
├── backend/
│   ├── main.py           # FastAPI entry point
│   ├── app.py            # Core application logic
│   └── requirements.txt  # Backend dependencies
├── frontend/
│   ├── ui.py             # Streamlit interface
│   └── requirements.txt  # Frontend dependencies
├── .env                  # Environment variables (API Keys)
├── .gitignore
└── README.md
