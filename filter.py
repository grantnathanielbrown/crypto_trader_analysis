import json
import re

# Define the list of specified authors, 'L', 'Rowdy✨ (villian arc)', 'unipcs'
specified_authors = ['user1777290290', 'user1404530968', 'user6038719888']  # Add the author names here

# Ethereum address pattern
eth_address_pattern = re.compile(r'\b0x[a-fA-F0-9]{40}\b')

# Load your JSON file
with open('./chat_history_until_dec10.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract the messages list from the JSON data
messages = data['messages']

# Function to find Ethereum addresses in a text
def find_eth_addresses(text):
    # If 'text' is not a string, return an empty list
    if not isinstance(text, str):
        return []

    # If 'text' is a string, find and return Ethereum addresses
    return eth_address_pattern.findall(text)


# Function to format the date
def format_date(date_str):
    # Assuming date_str is in ISO 8601 format '2023-11-01T13:27:04'
    return date_str.replace('T', ' ')  # Replace 'T' with a space for Google Sheets

# Start processing the messages
filtered_messages = []

for message in messages:
    # Check if the message is from a specified author
    if message.get('from_id') in specified_authors:
        eth_addresses = find_eth_addresses(message.get('text', ''))
        # print(message.get('text', ''))
        # If there is at least one Ethereum address in the message
        if eth_addresses:
            # Extract and format the required information
            for eth_address in eth_addresses:
                author = message['from']
                date_time = format_date(message['date'])
                unix_timestamp = message['date_unixtime']
                filtered_messages.append((author, eth_address, date_time, unix_timestamp))

# Format the data for Google Sheets
output_lines = ['Source,ETH Address,Date/Time,Unix Timestamp']
output_lines += [','.join(info) for info in filtered_messages]

# write directly to a file
output_file = 'output.csv'
with open(output_file, 'w', encoding='utf-8') as f:
    for line in output_lines:
        f.write(line + '\n')
