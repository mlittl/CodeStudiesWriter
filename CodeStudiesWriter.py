import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import requests

# Constants
URL = "http://localhost:11434/api/chat"
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

def select_file():
    """Prompt the user to select a file using a file dialog."""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def select_location():
    """Prompt the user to select a directory using a directory dialog."""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()

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
                "content": "You are a student who just finished writing this code. You want to summarize the outcomes of your learning via documentation. You want to emphasize how this helped you learn and expand your coding skillset. You want to write it as if you were a human technical writer. You MUST use markdown syntax. You MUST have an Overview section. You MUST have a Learnings section. You MUST have a section dedicated to a Conclusion of the learning outcomes. You MUST split the learnings into learning categories by perceived developer skill level, for example 'Beginner', 'Advanced' or 'Expert' skill levels. You MUST be extremely detailed. Go Step By Step. Take this code file and summarize it accordingly using markdown syntax: " + file_contents
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
            try:
                message = json.loads(line)
                message_contents += message['message']['content']
            except KeyError:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("Error parsing the file","Do you have the correct local LLM downloaded?")
                exit()
    return message_contents

def write_readme(file_path, message_contents, location):
    """Write the message contents to a README file."""
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    readme_path = os.path.join(location, f'{base_name}_learnings_README.md')
    with open(readme_path, 'w') as file:
        file.write(message_contents)
    return readme_path


def success_message(readme_path):
    """Show a success message."""
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Success", f"The README file has been successfully created at {readme_path}.")

def main():
    """Main function to run the program."""
    file_path = select_file()
    location = select_location()
    file_contents = read_file(file_path)
    check_server(URL)
    response = send_request(URL, file_contents)
    message_contents = parse_response(response)
    readme_path = write_readme(file_path, message_contents, location)
    success_message(readme_path)

if __name__ == "__main__":
    main()