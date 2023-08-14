import string

def word_frequency(text):
    # Convert text to lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text into words
    words = text.split()
    
    # Count word frequencies
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    return freq_dict

def display_word_frequencies(freq_dict):
    print("Word Frequencies:")
    for word, freq in freq_dict.items():
        print(f"{word}: {freq}")

# Get input from the user
user_input = input("Enter some text: ")

# Calculate word frequencies
frequency_dict = word_frequency(user_input)

# Display word frequencies
display_word_frequencies(frequency_dict)
