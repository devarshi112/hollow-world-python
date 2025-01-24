def get_greeting():
    """Returns the greeting string."""
    return "Hollow world!"

def get_greeting_wrapper():
    """Wrapper function to get and print the greeting."""
    greeting = get_greeting()
    print(greeting)