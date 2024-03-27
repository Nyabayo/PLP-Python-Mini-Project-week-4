import json
from difflib import get_close_matches

# Load the JSON data
def load_data(filename):
    # Using the provided absolute path
    path = r"C:\Users\ERNEST\OneDrive\Documents\Python 2024\Python programs\Week 4 Mini Project\dictionary-data\data.json"
    with open(path, "r") as file:
        return json.load(file)

# Find the word's definition
def define_word(dictionary, word):
    word = word.lower()
    if word in dictionary:
        return "\n".join(dictionary[word])
    else:
        suggestions = get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)
        if suggestions:
            return f"Did you mean '{suggestions[0]}'? Please check the spelling."
        else:
            return "The word doesn't exist. Please double-check it."

# Main function to run the dictionary app
def main():
    dictionary = load_data("data.json")  # This argument is not used anymore, consider removing it or adjusting your function definition
    word = input("Enter a word: ")
    print(define_word(dictionary, word))

if __name__ == "__main__":
    main()
