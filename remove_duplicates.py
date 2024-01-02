import csv

input_file = 'output.csv'  # Your original CSV file
output_file = 'no_duplicates.csv'  # The new CSV file without duplicates

# Read the CSV and store data
unique_addresses = set()
rows_to_keep = []

with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Assuming the first row is the header
    for row in reader:
        # Assuming the Ethereum address is the second column
        eth_address = row[1]
        if eth_address not in unique_addresses:
            unique_addresses.add(eth_address)
            rows_to_keep.append(row)

# Write the data back to another CSV, excluding duplicates
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    for row in rows_to_keep:
        writer.writerow(row)

print(f"Processed file saved as {output_file}")
