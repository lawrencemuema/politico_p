import re

class Validations:
    def validate_email(self, email):
    #email format only
        return re.match("^[^@]+@[^@]+\.[^@]+$", email)

    def validate_phone_number(self, phoneNumber):
     #phone must start and end with digit
     #10 digit only
        return re.match(r'^\d{4}-\d{3}-\d{3}$', phoneNumber)

    def validate_input_fields(self, input_fields):
    #input fields register only characters
        return re.match("^[a-zA-Z]{3,}", input_fields)

    def validate_password(self, password):
        return re.match("^[a-zA-Z0-9]{3,10}$", password)

    def validate_is_admin(self, isAdmin):
    #isadmin is bool, 1 or 0
        return re.match("^[0-1]{,1}$", isAdmin)

    def validate_url(self, url):
     #properly define a url
        return re.search(r"^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,}(?:/[^/#?]+)+\.(?:jp?g|gif|png)$", url)

    def validate_urls_id(self, id):
     #check if digit is provided
        return re.match("^[1-9]\d$", id)