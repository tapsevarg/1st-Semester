# This is a program to format string inputs


def input_text():
    print("Please enter a line of text to be formatted.")
    text = input()
    return text


def process_text(text):
    text = (text.strip()[::-1])
    return text


def output_text(text):
    print(text)


def main():
    text = input_text()
    text = process_text(text)
    output_text(text)


main()
