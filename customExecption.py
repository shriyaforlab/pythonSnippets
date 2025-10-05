
class InvalidAgeError(Exception):
    """"Raised when the age is invalid"""
    pass


def get_age():
    try:
        age = int(input("Enter your age: "))
        if age < 1 or age > 120:
            raise InvalidAgeError("Enter valid age")
        else:
            return age
    except InvalidAgeError as e:
        print("Error: ", e)
    except ValueError:
        print("Enter a valid age")

get_age()