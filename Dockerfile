# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /interview

# Copy the local script and input file to the container
COPY main.py /interview/main.py
COPY input.txt /interview/input.txt

# Run the Python script when the container starts
CMD ["python", "main.py"]