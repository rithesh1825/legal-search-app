# ⚖️ Legal Search App – Legal Information Search Platform

<p align="center">
  <b>A Simple Web-Based Legal Information Search Application</b>
  <br>
  Search legal case information through an intuitive interface with multilingual support.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5">
  <img src="https://img.shields.io/badge/CSS3-Styling-blue?logo=css3">
  <img src="https://img.shields.io/badge/JSON-Data-lightgrey?logo=json">
</p>

---

## 📌 Overview

Legal Search App is a Python Flask-based web application designed to make legal information easier to explore and access.

The application allows users to register, log in, and search through a collection of legal case information using keywords. It supports English and Hindi case summaries, making legal information accessible through a simple and user-friendly interface.

The project demonstrates the integration of Python backend development, frontend technologies, JSON-based data management, and multilingual search functionality.

## ✨ Key Features

🔍 **Legal Case Search**
- Search legal cases using keywords.
- Retrieve matching case titles and summaries.
- Display relevant search results.

🌐 **Multilingual Support**
- English language summaries.
- Hindi language summaries.
- Language-based search functionality.

🔐 **User Authentication**
- User registration interface.
- Login functionality.
- Session-based navigation.

💻 **Interactive Web Interface**
- Login page.
- Registration page.
- Legal search interface.
- Search results page.
- Custom CSS styling.

📁 **JSON-Based Data Management**
- Store legal case information in JSON format.
- Load and process case records using Python.
- Support structured legal information.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML5 | Frontend structure |
| CSS3 | User interface styling |
| JavaScript | Frontend scripting, if used |
| JSON | Legal case data storage |

## 🏗️ Application Workflow

```text
          USER
            |
            ▼
       LOGIN / REGISTER
            |
            ▼
       LEGAL SEARCH PAGE
            |
            ▼
       ENTER SEARCH QUERY
            |
            ▼
       FLASK BACKEND
            |
            ▼
       LOAD CASES.JSON
            |
            ▼
       KEYWORD MATCHING
            |
            ▼
       FILTER SEARCH RESULTS
            |
            ▼
       DISPLAY MATCHING CASES
```

## 📂 Project Structure

```text
legal-search-app/
│
├── app.py
│
├── cases.json
│
├── login.html
│
├── register.html
│
├── chat.html
│
├── results.html
│
├── style.css
│
├── hathoda.jpg
│
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rithesh1825/legal-search-app.git
```

### 2. Navigate to the Project Directory

```bash
cd legal-search-app
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Flask

```bash
pip install flask
```

### 5. Organize Flask Templates

Flask expects HTML templates inside a `templates` directory and static assets such as CSS inside a `static` directory.

Organize the files as follows:

```text
legal-search-app/
│
├── app.py
├── cases.json
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── chat.html
│   └── results.html
│
├── static/
│   ├── style.css
│   └── hathoda.jpg
│
└── README.md
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open in Browser

```text
http://127.0.0.1:5000
```

Register an account, log in, and explore the legal search interface.

## 🔎 Search Functionality

The application supports keyword-based searching through legal case records.

Example search queries:

- Murder Case
- Criminal Law
- Legal Information

Users can choose between English and Hindi summaries.

The search functionality compares the entered query against case titles and summaries stored in the JSON dataset.

## 🎯 Project Objectives

- Build a web-based legal information search platform.
- Develop backend applications using Python and Flask.
- Implement keyword-based search functionality.
- Support multilingual legal information.
- Understand session management and web authentication.
- Manage structured information using JSON.

## 🔮 Future Enhancements

- Integrate AI-powered legal question answering.
- Implement semantic search using NLP.
- Add a larger legal case database.
- Integrate Retrieval-Augmented Generation (RAG).
- Add PDF legal document uploads.
- Implement secure database-backed authentication.
- Add advanced search filters.
- Develop an admin dashboard.
- Deploy the application to a cloud platform.

## 👨‍💻 Author

**Rithesh K**

GitHub: [@rithesh1825](https://github.com/rithesh1825)

Project: [Legal Search App](https://github.com/rithesh1825/legal-search-app)

---

## ⚠️ Disclaimer

This application is an educational project designed for exploring legal information.

It does not provide professional legal advice. Information should be independently verified using authoritative legal sources.

---

<p align="center">
  ⭐ If you find this project interesting, consider giving the repository a star!
  <br><br>
  <b>Built with ❤️ by Rithesh K</b>
</p>
