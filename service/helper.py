"""Returns the greeting string."""
def get_greeting():
    return "Hollow world!"

"""Wrapper function to get and print the greeting."""
def get_greeting_wrapper():
    greeting = get_greeting()
    print(greeting)

"""Given a string, replace all spaces with '%20'. Trim leading and trailing spaces."""
def urlify_string(s):
    if s is None:
        return None
    return s.strip().replace(' ', '%20')

"""Wrapper function to for the urlify_string function."""
def urlify_string_wrapper():
    print(urlify_string(None))
    print(urlify_string(""))
    print(urlify_string("John Smith"))
    print(urlify_string(" John Smith  "))
    print(urlify_string("John   Smith  "))
    print(urlify_string("John   "))
    print(urlify_string("   Smith"))
    print(urlify_string("www.test.com/I Love Coding  "))