def hello_world():
    """Return a hello world message."""
    return "Hello, World!"


def main():
    """Main entry point of the application."""
    message = hello_world()
    print(message)
    return message


if __name__ == "__main__":
    main()
