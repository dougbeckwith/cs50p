import validators


def main():
    email = prompt_user_email_address()
    status = validate_email(email)
    print(status)


def prompt_user_email_address():
    return input("What's your email address? ")


def validate_email(email):
    if not validators.email(email):
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()
