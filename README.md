# Python Bigram Analysis with Docker :whale2:

This repository contains two implementations of bigram analysis:

1. A standalone Python script.
2. A Flask-based web API.

## Prerequisites

- [Docker](https://www.docker.com/get-started) must be installed on your system.

## Example Input File
An example input file (`input.txt`) has been provided in this repository. You can use it for testing the script.
Click on a section below to view the relevant instructions.

## Steps

### 1. Clone the Repository

Clone this repository to your local machine:

```shell
git clone https://github.com/lenulef1/python-bigram-analysis.git
```

### 2. Navigate to the right dierctory

Navigate to the repository directory:

```shell
cd python-bigram-analysis
```

<details open>
<summary><strong>Python Script</strong></summary>

### 3. Build the Docker Image

Build the Docker image:

```shell
docker build -t bigram-app .
```

### 4. Run the Docker Container

Run the Docker container to analyze the example input file (`input.txt`):

```shell
docker run bigram-app
```

### 5.  View the Results

The script will analyze the example input file and print the top 10 most frequent bigrams to the console.

</details>

<details open>
<summary><strong>Flask Web API</strong></summary>
<br>

This section contains instructions for setting up and interacting with the Flask web API:

### 3. Build the Docker Image

Build the Docker image:

```shell
docker build -t flask-bigram-app -f Dockerfile_flask .
```

### 4. Run the Docker Container

Run the Docker container and map port 5000:

```shell
docker run -p 5000:5000 flask-bigram-app
```

<details open>
  <summary><i>Interact with the Web API with POST method</i></summary>

### 5. Interact with the Web API

The Flask web API will be accessible at `http://localhost:5000/upload`. You can use tools like `curl` or Postman to send a POST request with a file to this endpoint:

Using `curl`:

```shell
curl -X POST -F "file=@input.txt" http://127.0.0.1:5000/upload
```

Using Postman:

- Set the request type to POST.
- Enter the URL: `http://127.0.0.1:5000/upload`.
- In the "Body" tab, select "form-data".
- Add a key named "file", set its type to "File", and then select the file you want to upload.
- Send the request.

The response will contain the top 10 most frequent bigrams from the uploaded file in JSON format.
</details>

<details open>
  <summary><i>Analyze a Wikipedia Article with GET method</i></summary>

### 5. Interact with the Web API

Send a GET request to the endpoint `http://localhost:5000/wikipedia/<article_name>`, replacing `<article_name>` with the name of a Wikipedia article:

Using `curl`:

```shell
curl http://127.0.0.1:5000/wikipedia/Merck_Group
```

Using Postman:

- Set the request type to GET.
- Enter the URL: `http://127.0.0.1:5000/wikipedia/Merck_Group`.
- Send the request.

The response will contain the top 10 most frequent bigrams from the specified Wikipedia article in JSON format.
</details>

</details>
