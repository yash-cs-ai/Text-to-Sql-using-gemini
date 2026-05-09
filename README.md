# Text to SQL application via Gemini

A Streamlit application that uses Google's Gemini AI to convert natural language questions into SQL queries, executes them on a local SQLite database, and displays the result.

## 🛠️ Tech Stack

* **Python 3.10+**
* **Streamlit** (Frontend)
* **Google GenAI SDK** (`google-genai`)
* **SQLite** (Database)

## 📋 Prerequisites

1. **Google Gemini API Key:**
    * Get your free key here: [Google AI Studio](https://aistudio.google.com/app/apikey)

2. **Python Installed:** Make sure Python is installed on your system.

## ⚙️ Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yash-cs-ai/Text-to-Sql-using-gemini.git
    cd your-repo-name
    ```

2. **Create a virtual environment (Optional but Recommended):**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install streamlit google-genai python-dotenv pandas
    ```

4. **Set up Environment Variables:**

    Create a file named `.env` in the root folder and add your API key:

    ```env
    GEMINI_API_KEY="your_google_api_key_here"
    ```

## 🗄️ Database Setup

Before running the app, you need to create the dummy database.

1. Create a file named `sqlite.py` (if not already present) with the database creation logic.
2. Run the script to generate `student.db`:

    ```bash
    python sqlite.py
    ```

    *This will create the `student.db` file with sample data (Name, Class, Section).*

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run sql.py
