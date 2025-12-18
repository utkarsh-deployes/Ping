import requests
import os
import smtplib
from email.mime.text import MIMEText

API_URL = "https://remotive.com/api/remote-jobs"

KEYWORDS = [
    "python", "data", "analyst", "ai", "backend",
    "software", "developer", "engineer", "machine learning", "ml"
]

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def get_jobs():
    res = requests.get(API_URL, timeout=15)
    res.raise_for_status()
    return res.json()["jobs"]


def is_relevant(title):
    title = title.lower()
    return any(k in title for k in KEYWORDS)


def send_email(jobs):
    if not all([SENDER_EMAIL, RECEIVER_EMAIL, EMAIL_PASSWORD]):
        print("❌ Email credentials missing")
        return

    body = ""
    for job in jobs:
        body += f"{job['title']} | {job['company_name']}\n{job['url']}\n\n"

    msg = MIMEText(body)
    msg["Subject"] = "🔥 Daily Job Tracker"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)

    print("📧 Email sent successfully")


def main():
    jobs = get_jobs()

    relevant_jobs = [
        job for job in jobs if is_relevant(job["title"])
    ]

    print(f"Total jobs fetched: {len(jobs)}")

    if relevant_jobs:
        send_email(relevant_jobs)
        print(f"🔥 {len(relevant_jobs)} relevant jobs emailed")
    else:
        print("😴 No relevant jobs today")


if __name__ == "__main__":
    main()
