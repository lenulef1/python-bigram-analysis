# Python Bigram Analysis with Docker

This repository contains a Python script that analyzes the top 10 most frequently occurring pairs of successive words (bigrams) in a text file using Docker.

## Prerequisites

- [Docker](https://www.docker.com/get-started) must be installed on your system.

## Usage

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

## Example Input File
An example input file (`input.txt`) has been provided in this repository. You can use it for testing the script.