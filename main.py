def greet(name):
    return f"Hello, {name}. Practising Git with Python!"
if __name__=="__main__":
    message = greet("Vasilka")
    print(message)


def greet(name):
    return f"Hello, {name}. Practising Git with Python!"
if __name__=="__main__":
    user_name = input("Enter your name:")
    print(greet(user_name))