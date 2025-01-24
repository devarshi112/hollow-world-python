from service.helper import get_greeting

def main():
    """Main method to invoke the helper functions."""
    greeting = get_greeting()
    print(greeting)

if __name__ == "__main__":
    main()