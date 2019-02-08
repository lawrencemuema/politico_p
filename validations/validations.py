import re


class Validations:
    def validate_email(self, email):
        """ validate for email """
        return re.match("^[^@]+@[^@]+\.[^@]+$", email)

    def validate_phone_number(self, phoneNumber):
        """phone number must start with a digit and end with
        a digit, and must be ten digits onnly """
        return re.match(r'^\d{4}-\d{3}-\d{3}$', phoneNumber)

    def validate_input_fields(self, input_fields):
        """ validate input fields to accept characters only """
        return re.match("^[a-zA-Z]{3,}", input_fields)

    def validate_password(self, password):
        """ validate password """
        return re.match("^[a-zA-Z0-9]{3,10}$", password)

    def validate_is_admin(self, isAdmin):
        """ validate if is admin is between the range of 1 and 0 """
        return re.match("^[0-1]{,1}$", isAdmin)

    def validate_url(self, url):
        """ function to validate url """
        return re.search(r"^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,}(?:/[^/#?]+)+\.(?:jp?g|gif|png)$", url)

    def validate_urls_id(self, id):
        """ check if the url is valid """
        return re.match("^[1-9]\d$", id)