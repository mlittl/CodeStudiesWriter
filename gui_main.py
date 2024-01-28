import os
import json
import requests
import tkinter as tk
from tkinter import filedialog

def select_file():
    """Prompt the user to select a file using a file dialog."""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def read_file(file_path):
    """Read the contents of a file."""
    with open(file_path, 'r') as file:
        return file.read()

def check_server(url):
    """Check if the server is running."""
    try:
        requests.get(url)
    except requests.exceptions.RequestException:
        print("The server is not running. Please run 'ollama serve' and try again.")
        exit()

def send_request(url, file_contents):
    """Send a POST request to the server."""
    data = {
        "model": "openhermes",
        "messages": [
            {
                "role": "user",
                "content": "You are a student who just finished writing this code. You want to summarize the outcomes of your learning via documentation. You want to emphasize how this helped you learn for your coding skillset. You want to write it as if you were a human and not an AI or LLM. You must use markdown syntax. You must have a Summary and Learnings section, at minimum. You must have a section dedicated to a conclusion of the learnings. Take this code file and summarize it accordingly using markdown syntax: " + file_contents
            }
        ]
    }
    return requests.post(url, data=json.dumps(data))

def parse_response(response):
    """Parse the response from the server."""
    response_lines = response.text.split('\n')
    message_contents = ""
    for line in response_lines:
        if line:
            message = json.loads(line)
            message_contents += message['message']['content']
    return message_contents

def write_readme(file_path, message_contents):
    """Write the message contents to a README file."""
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(f'{base_name}_Learnings_README.md', 'w') as file:
        file.write(message_contents)

def main():
    """Main function to run the program."""
    file_path = select_file()
    file_contents = read_file(file_path)
    url = "http://localhost:11434/api/chat"
    check_server(url)
    response = send_request(url, file_contents)
    message_contents = parse_response(response)
    write_readme(file_path, message_contents)

if __name__ == "__main__":
    main()