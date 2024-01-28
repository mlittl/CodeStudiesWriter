import requests
import json
import os

# Define the path to the Python file
file_path = '/home/golliath/Desktop/Code/100 Days/day8/second.py'

# Read the contents of the Python file
with open(file_path, 'r') as file:
    file_contents = file.read()

url = "http://localhost:11434/api/chat"
data = {
  "model": "openhermes",
  "messages": [
    {
      "role": "user",
      "content": "You are a student who just finished writing this code. You want to summarize the outcomes of your learning via documentation. You want to emphasize how this helped you learn for your coding skillset. You want to write it as if you were a human and not an AI or LLM. Take this code file and summarize it accordingly using markdown syntax: " + file_contents
    }
  ]
}

response = requests.post(url, data=json.dumps(data))

# Split the response text by newline characters
response_lines = response.text.split('\n')

# Initialize an empty string to store the message contents
message_contents = ""

# Iterate over the lines in the response
for line in response_lines:
    # Ignore empty lines
    if line:
        # Parse the line as a JSON object
        message = json.loads(line)
        # Add the content of the message to the string
        message_contents += message['message']['content']

# Get the base name of the Python file (without the extension)
base_name = os.path.splitext(os.path.basename(file_path))[0]

# Create a new README file named after the Python file
with open(f'{base_name}_Learnings_README.md', 'w') as file:
    file.write(message_contents)

