# README for Python Code Documentation Project (Autodoc)
## Introduction
This is a Python script designed to facilitate the documentation of learning outcomes from coding experiences. The primary objective of this script is to assist users in summarizing and reflecting on their coding journey, specifically focusing on how their skillset has evolved. This tool aims to capture the essence of learning through code, providing a unique perspective that mimics a human-like understanding and articulation of the learning process.

## Installation

Before running this script, ensure you have Python installed on your system. Additionally, the script requires the requests library for sending HTTP requests and the json library for handling JSON data. Follow these steps to set up the environment:

    Install Python: Download and install Python from python.org.
    Install Required Libraries: Run the following command to install the necessary libraries:

    bash

    pip install requests
    pip install ollama
    ollama run openhermes (OR ANY MODEL OF YOUR CHOOSING)

## Usage

To use this script, follow these steps:

    Prepare Your Code File: Have the Python file ready to be read.
    Run the Script: Execute the script. It will read your Python file that you select via the GUI, send its contents to a predefined API endpoint, and receive a response summarizing the learning outcomes.
    View the Output: The script generates a README file (<base_name>_Learnings_README.md) containing the summarized learning outcomes. It will be in the same directory of this script.

## How It Works

    The script reads the contents of a specified Python file.
    It sends these contents to a local API endpoint (http://localhost:11434/api/chat) using an HTTP POST request. The data includes a model identifier (openhermes) and the file contents as a message.
    The script processes the response from the API, extracting and compiling the meaningful content.
    Finally, it generates a markdown README file, summarizing the learning outcomes derived from the code.

## Contributing

Contributions to enhance this project are welcome. To contribute:

    Fork the Repository: Create a copy of this project to your GitHub account.
    Make Your Changes: Implement your improvements or fixes.
    Submit a Pull Request: Propose your changes for review and integration into the main project.

Please ensure your contributions adhere to best coding practices and do not break existing functionality.
Notes

    This script assumes the presence of a local API and does not handle errors related to network issues or API unavailability.
    Modifications might be needed based on the specific setup of your local environment and the API endpoint.

For any queries or issues, please open an issue in the project's GitHub repository. This project is a stepping stone in understanding and documenting the coding learning journey in a more humanized and reflective manner.
