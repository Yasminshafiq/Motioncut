def count_words(text):
    # Split the text into words using spaces and count the length of the resulting list
    words = text.split()
    return len(words)

# Main function to run the program
def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Enter a sentence or paragraph: ").strip()

    # Check if the input is empty and handle the error
    if not user_input:
        print("Error: You entered an empty text. Please provide a valid sentence or paragraph.")
    else:
        # Call the count_words function and display the result
        word_count = count_words(user_input)
        print(f"The number of words in the given text is: {word_count}")

# Entry point of the program
if __name__ == "__main__":
    main()
