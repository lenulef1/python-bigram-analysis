# Importing necessary libraries for the Flask app
from flask import Flask, request, jsonify
import re
from collections import Counter

# Defining the Flask app
app = Flask(__name__)


# Function to process the uploaded file using the logic from the provided script
def process_file(file_content):
    # Extracting the relevant parts from the improved code for integration
    # Preprocess the Text
    words = re.findall(r'\b\w+\b', file_content.lower())  # Split text using whitespace or punctuation
    # Generate Bigrams
    bigrams = list(zip(words, words[1:]))
    # Count Bigram Frequencies
    bigram_counts = Counter(bigrams)
    # Find the Top 10 Most Frequent Bigrams
    return bigram_counts.most_common(10)


# Flask endpoint to accept file uploads and process them
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    file_content = file.read().decode('utf-8')
    results = process_file(file_content)

    # Formatting the results for JSON response
    formatted_results = [{"bigram": f"{bigram[0]} {bigram[1]}", "frequency": frequency} for bigram, frequency in
                         results]
    return jsonify(formatted_results)


# Main execution
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
