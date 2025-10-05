
def get_num():
    while True:
        try:
            value = int(input("Enter the number: "))
            return value
        except ValueError:
            print("Please enter a valid number")

get_num()



