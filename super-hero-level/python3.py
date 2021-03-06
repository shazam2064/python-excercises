# class Email:
#     def __init__(self, to, subject, body):
#         self.to = to
#         self.subject = subject
#         self.body = body
#
#     def send(self):
#         print(f"Sending email with subject: {self.subject} and body: {self.body} to: {self.to}")
#
#
# if __name__ == "__main__":
#     greeting_email = Email("bob@nasa.gov", "Welcome!", "Welcome to your mom's house!")
#     greeting_email.subject = "Greeting!"
#     greeting_email.to = "liz@buckingham.uk"
#     greeting_email.send()


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

    def send(self, to):
        print(f"Sending email with subject: {self.subject} and body: {self.body} to: {to}")


if __name__ == "__main__":
    greeting_email = Email("Welcome!", "Welcome to your mom's house!")
    greeting_email.subject = "Greeting!"
    greeting_email.send("bob@nasa.gov")
    greeting_email.send("liz@buckingham.uk")
