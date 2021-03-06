class Email:
    valid_domain = "jomamma.io"

    def __init__(self, subject, body, from_recipient):
        self.subject = subject
        self.body = body

        split = from_recipient.split("@")
        if split[1] != self.valid_domain:
            raise Exception("Invalid domain")

        self.__from_recipient = from_recipient

    @property
    def from_recipient(self):
        return self.__from_recipient

    @from_recipient.setter
    def from_recipient(self, from_recipient):
        split = from_recipient.split("@")
        if split[1] != self.valid_domain:
            raise Exception("Invalid domain")
        self.__from_recipient = from_recipient

    def send(self, to):
        print(
            f"Sending email from: {self.__from_recipient} with subject: {self.subject} and body: {self.body} to: {to}")


if __name__ == "__main__":
    greeting_email = Email("Welcome!", "Welcome to notjomamma.com!", "greeting@jomamma.io")
    bf_email = Email("Black Friday 2021!", "99% discount on our platform", "bf@jomamma.io")

    # Email.valid_domain = "notjomamma.com"
    greeting_email.valid_domain = "notjomamma.com"

    # greeting_email.from_recipient = "welcome@jomamma.io"
    greeting_email.from_recipient = "greeting@notjomamma.com"
    bf_email.from_recipient = "bf@notjomamma.com"
    # print(greeting_email.from_recipient)
    # greeting_email.subject = "Greeting!"

    greeting_email.send("bob@nasa.gov")
    bf_email.send("alex@gmail.com")
    # greeting_email.send("liz@buckingham.uk")
