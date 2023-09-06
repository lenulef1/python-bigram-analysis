# Python Bigram Analysis with Docker

This repository contains two implementations of bigram analysis:

1. A standalone Python script.
2. A Flask-based web API.

## Prerequisites

- [Docker](https://www.docker.com/get-started) must be installed on your system.

## Example Input File
An example input file (`input.txt`) has been provided in this repository. You can use it for testing the script.
Click on a section below to view the relevant instructions.

<details>
<summary><strong>Python Script</strong></summary>

Follow these steps to run the basic Python script:

### 1. Clone the Repository

Clone this repository to your local machine:

```shell
git clone https://github.com/lenulef1/python-bigram-analysis.git
```

### 2. Build the Docker Image

Navigate to the repository directory:

```shell
cd python-bigram-analysis
```

Build the Docker image:

```shell
docker build -t bigram-app .
```

### 3. Run the Docker Container

Run the Docker container to analyze the example input file (`input.txt`):

```shell
docker run bigram-app
```

### 4.  View the Results

The script will analyze the example input file and print the top 10 most frequent bigrams to the console.

</details>

<details>
<summary><strong>Flask Web API</strong></summary>
<br>

This section contains instructions for setting up and interacting with the Flask web API:

### 1. Clone the Repository

```shell
git clone https://github.com/lenulef1/python-bigram-analysis.git
```

### 2. Build the Docker Image

Navigate to the repository directory:

```shell
cd python-bigram-analysis
```

Build the Docker image:

```shell
docker build -t flask-bigram-app -f Dockerfile_flask .
```

### 3. Run the Docker Container

Run the Docker container and map port 5000:

```shell
docker run -p 5000:5000 flask-bigram-app
```

### 4. Interact with the Web API

The Flask web API will be accessible at `http://localhost:5000/upload`. You can use tools like `curl` or Postman to send a POST request with a file to this endpoint:

Using `curl`:

```shell
curl -X POST -F "file=@path_to_your_file.txt" http://127.0.0.1:5000/upload
```

Using Postman:

- Set the request type to POST.
- Enter the URL: `http://127.0.0.1:5000/upload`.
- In the "Body" tab, select "form-data".
- Add a key named "file", set its type to "File", and then select the file you want to upload.
- Send the request.

The response will contain the top 10 most frequent bigrams from the uploaded file in JSON format.

</details>