import re

class Validation:
    
    def __init__(self):
        self.is_valid = False

    # check for Integers
    def check_for_int(self, word):
        a = []
        for i in word:
            if(i.isdigit()):
                a.append(i)
        if(len(a)>=1):
           self.is_valid = True
        else:
           self.is_valid = False
        return self.is_valid

    # check for white_space between words
    def check_white_space(self, word):
        a = []
        for i in word:
            if(i.isspace()):
                a.append(i)
        if(len(a)>=1):
           self.is_valid = True
        else:
           self.is_valid = False
        return self.is_valid

    # check for white
    def validate_password(self, password:str):
        self.is_valid = False
        if (len(password)>=8 and not password.islower() 
            and not password.isupper() 
            and self.check_for_int(password) 
            and not self.check_white_space(password)):
           self.is_valid = True
        else:
           self.is_valid = False
        return self.is_valid

    def detect_special_characters(self, pass_string:str):
        import re
        regex= re.compile('[@!#$%^&*()<>?/\\\|}{~:[\]`_]')
        if(regex.search(pass_string) == None): 
            self.is_valid = False
        else: 
            self.is_valid = True
        return self.is_valid

    def detect_dashes(self, pass_string):
        import re
        regex= re.compile('[-]')
        if(regex.search(pass_string) == None): 
            self.is_valid = False
        else: 
            self.is_valid = True
        return self.is_valid

    def is_empty(self, pass_string):
        if not pass_string:
            self.is_valid = True
        else: 
            self.is_valid = False
        return self.is_valid

    def validate_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, email):
            self.is_valid = True
        else:
            self.is_valid = False
        return self.is_valid
        