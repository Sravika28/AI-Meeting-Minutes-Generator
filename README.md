# AI Meeting Minutes Generator

## Project Overview

The AI Meeting Minutes Generator is a Generative AI application that converts raw meeting notes into professional meeting minutes using a Large Language Model (LLM).

The application automatically generates:

- Meeting Summary
- Action Items
- Professional Follow-up Email

This project is built using Python, Streamlit, and the Groq API with the Llama 3.3 model.

---

## Features

- Generate concise meeting summaries
- Extract action items
- Create professional follow-up emails
- Simple and user-friendly Streamlit interface
- Secure API key management using `.env`

---

## Technologies Used

- Python
- Streamlit
- Groq API
- Llama 3.3 70B Versatile
- Prompt Engineering
- dotenv

---

## Project Structure

```
AI-Meeting-Minutes-Generator/
│
├── app.py
├── ai_helper.py
├── .gitignore
├── README.md
├── requirements.txt
└── .env (not uploaded)
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sravika28/AI-Meeting-Minutes-Generator.git
```

Move into the project folder:

```bash
cd AI-Meeting-Minutes-Generator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Output

The application generates:

- Meeting Summary
- Action Items
- Professional Follow-up Email

from simple meeting notes.

---

## Future Improvements

- Download meeting minutes as PDF
- Download as Word document
- Meeting history
- Copy to clipboard
- Better UI
- Authentication
- Cloud Deployment

---

## Author

**Sravika**