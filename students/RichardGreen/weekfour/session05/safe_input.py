
'''The raw_input() function can generate two exceptions: - EOFError or
end-of-file (EOF) - KeyboardInterrupt or canceled input. - Create a wrapper
function, perhaps safe_input() that returns None rather than raising these
exceptions.'''


def safe_input():

    try:
        return raw_input("Enter values:")
    except (KeyboardInterrupt, TypeError, ValueError, EOFError):
        None

if __name__ == "__main__":
    #
    print safe_input()
