import re
from collections import Counter

def main():
    # Step 1: Read the Input File
    input_file = "input.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        return

    # Step 2: Preprocess the Text
    words = re.findall(r'\b\w+\b', text.lower())  # Split text into words using whitespace or punctuation

    # Step 3: Generate Bigrams
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]

    # Step 4: Count Bigram Frequencies
    bigram_counts = Counter(bigrams)

    # Step 5: Find the Top 10 Most Frequent Bigrams
    top_10_bigrams = bigram_counts.most_common(10)

    # Step 6: Print the Results
    print("Top 10 Most Frequent Bigrams:")
    for bigram, frequency in top_10_bigrams:
        print(f"{bigram[0]} {bigram[1]} - Frequency: {frequency}")

if __name__ == "__main__":
    main()
