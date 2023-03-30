"""Things I'll be importing"""

def addition(x: int, y: int) -> int:
    return x + y

my_variable: str = "Hello!"

if __name__ == "main":
    print("This should only print when running my_functions")
else:
    print("my_functions is being imported")