# 🗞️ Tech News Email Notifier

This Python script fetches the latest tech headlines from TechCrunch using the NewsAPI and emails them directly to your inbox. It's a lightweight, automated way to stay up to date with trending technology stories.

---

## 🚀 Features

- Retrieves top 20 tech headlines from TechCrunch
- Extracts article title, description, and URL
- Sends the news digest as a formatted email
- Encodes to ASCII to avoid encoding issues
- Uses environment variables for secure credentials

---

## 🛠 Technologies Used

- `requests` for API access
- `smtplib` and `ssl` for sending secure emails
- `python-dotenv` (recommended) to store your credentials safely

---

## 📦 File Overview

- `main.py`: Fetches news articles and sends them via email
- `send_email.py`: Handles email composition and delivery
- `.env`: Stores your Gmail app password securely (not included by default)

---

📘 Real-World Applications- Personal morning briefing via email
- Lightweight serverless news alert system
- News aggregation for internal tech teams