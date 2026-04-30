#!/usr/bin/env python3
"""Minimal contact form relay for vitrine-kit sites."""
import os, smtplib
from email.message import EmailMessage


def load_settings(path="deploy/settings.env"):
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k, v)


def send(name, email, message):
    if os.path.exists("deploy/settings.env"):
        load_settings()
    msg = EmailMessage()
    msg["Subject"] = f"[contact] {name}"
    msg["From"] = os.environ["SMTP_USER"]
    msg["To"] = os.environ["MAIL_TO"]
    msg["Reply-To"] = email
    msg.set_content(message)
    with smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ.get("SMTP_PORT", 587))) as s:
        s.starttls()
        s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
        s.send_message(msg)
