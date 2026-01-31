# Steps to Run the Project

## Prerequisites
* Python 3.9 or above
* Ollama (Ensure the service is running)
* Git
* Installed Libraries: `fastapi`, `uvicorn`, `streamlit`

---

## How to Start

1.  **Clone the Repository**
    ```bash
    git clone <repository-url>
    ```

2.  **Start the Backend**
    Navigate to the backend folder, install dependencies, and start the server:
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
    *(Keep this terminal open)*

3.  **Start the Frontend**
    Open a **new terminal**, navigate to the frontend folder, and launch the UI:
    ```bash
    cd frontend
    streamlit run app.py
    ```

4.  **Interact**
    Open your browser (auto-opens at `http://localhost:8501`) to use the chatbot.