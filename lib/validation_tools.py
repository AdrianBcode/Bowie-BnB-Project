



class ValidationTools:
    def __init__(self):
        pass

    def password_validator(self, input: str, specialchars, pass_length: int) -> bool:
        if len(input) >= pass_length and set(input).intersection(set(specialchars)):
            return True
        return False
    
    # #  Parameters:
    #     input: the password string to be validated
    #     specialchars: the special characters you require in the password
    #     pass_length: the minimum length you wish for the password to be

