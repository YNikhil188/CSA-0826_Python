class CustomException(Exception):
    def __init__(self, message="This is a custom exception."):
        self.message = message
        super().__init__(self.message)

def example_function(x):
    if x < 0:
        raise CustomException("Number cannot be negative.")

try:
    num = int(input("Enter a number: "))
    example_function(num)
except CustomException as e:
    print("CustomException:", e)