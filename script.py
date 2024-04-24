import nltk
from nltk.corpus import stopwords
from collections import Counter


nltk.download('punkt')
nltk.download('stopwords')

def read_text(file_path):

    with open(file_path, 'r') as file:
        text = file.read()
    return text

def remove_stopwords(text):
   
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def count_character_occurrences(text):
   
    text = text.replace(" ", "")  
    char_occurrences = Counter(text)
    return char_occurrences

def print_character_occurrences(char_occurrences):
   
    for char, occurrence in char_occurrences.items():
        print(f"The character '{char}' appears {occurrence} times.")

file_path = "/app/random_paragraphs.txt"

text = read_text(file_path)

filtered_text = remove_stopwords(text)

char_occurrences = count_character_occurrences(filtered_text)

print_character_occurrences(char_occurrences)

total_characters_original = sum(1 for char in text if char.isalnum())
total_characters_filtered = sum(1 for char in filtered_text if char.isalnum())

print(f"Total characters before filtering: {total_characters_original:,}")
print(f"Total characters after filtering: {total_characters_filtered:,}")