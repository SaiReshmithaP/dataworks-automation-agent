import subprocess
import json
import os
import datetime
from src.llm_handler import extract_email, extract_credit_card

def execute_task(task):
    if "install uv" in task and "run" in task:
        return subprocess.run(["pip", "install", "uv"], capture_output=True, text=True).stdout
    
    elif "format" in task and ".md" in task:
        return subprocess.run(["npx", "prettier", "--write", "/data/format.md"], capture_output=True, text=True).stdout

    elif "count Wednesdays" in task:
        with open("/data/dates.txt", "r") as file:
            dates = file.readlines()
        wednesdays = sum(1 for date in dates if datetime.datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)
        with open("/data/dates-wednesdays.txt", "w") as file:
            file.write(str(wednesdays))
        return f"Counted {wednesdays} Wednesdays"

    elif "sort contacts" in task:
        with open("/data/contacts.json", "r") as file:
            contacts = json.load(file)
        contacts.sort(key=lambda c: (c["last_name"], c["first_name"]))
        with open("/data/contacts-sorted.json", "w") as file:
            json.dump(contacts, file, indent=2)
        return "Contacts sorted"

    elif "extract email" in task:
        with open("/data/email.txt", "r") as file:
            email_content = file.read()
        sender_email = extract_email(email_content)
        with open("/data/email-sender.txt", "w") as file:
            file.write(sender_email)
        return "Email extracted"

    elif "extract credit card" in task:
        result = extract_credit_card("/data/credit-card.png")
        with open("/data/credit-card.txt", "w") as file:
            file.write(result)
        return "Credit card extracted"

    else:
        raise ValueError("Unsupported task")
