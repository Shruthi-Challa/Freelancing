def is_valid_email(email):
    if email is None:
        return False

    email = email.strip().lower()

    if email == "" or "@" not in email:
        return False

    return True


emails = [
    "shruthi@gmail.com",
    "",
    None,
    "tharun@yahoo.com",
    "shruthigmail.com"
]

valid_emails = []
invalid_emails = []

for email in emails:
    if is_valid_email(email):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

print("Valid emails:", valid_emails)
print("Invalid emails:", invalid_emails)