
# Importing necessary libraries for the Flask app
from flask import Flask, request, jsonify
import re
from collections import Counter
import requests
from bs4 import BeautifulSoup

# Defining the Flask app
app = Flask(__name__)

# Function to process the uploaded file using the logic from the provided script
def process_file(file_content):
    # Preprocess the Text
    words = re.findall(r'\b\w+\b', file_content.lower())  # Split text using whitespace or punctuation
    # Generate Bigrams
    bigrams = list(zip(words, words[1:]))
    # Count Bigram Frequencies
    bigram_counts = Counter(bigrams)
    # Find the Top 10 Most Frequent Bigrams
    return bigram_counts.most_common(10)

def fetch_wikipedia_content_via_api(article_name):
    # Fetching the Wikipedia page content using the Wikipedia API
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": article_name,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    page_content = next(iter(data["query"]["pages"].values()))["extract"]
    return page_content

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
    formatted_results = [{"bigram": f"{bigram[0]} {bigram[1]}", "frequency": frequency} for bigram, frequency in results]
    return jsonify(formatted_results)

# New Flask endpoint to process Wikipedia articles
@app.route('/wikipedia/<article_name>', methods=['GET'])
def process_wikipedia_article(article_name):
    content = fetch_wikipedia_content_via_api(article_name)
    results = process_file(content)
    # Formatting the results for JSON response
    formatted_results = [{"bigram": f"{bigram[0]} {bigram[1]}", "frequency": frequency} for bigram, frequency in results]
    return jsonify(formatted_results)

# Main execution
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
