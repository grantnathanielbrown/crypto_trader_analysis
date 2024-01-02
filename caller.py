import csv
import requests
import time
import os
from datetime import datetime, timedelta

def make_api_call(graphql_query):
    api_url = "https://graph.defined.fi/graphql"
    api_key = os.getenv('DEFINED_API_KEY')
    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }
    response = requests.post(api_url, json={"query": graphql_query}, headers=headers)
    if response:
        return response.json()
    else:
        return None

input_template = '{{address: "{address}", networkId: 1, timestamp: {timestamp}}}'

# Read the CSV and process each row
input_file = 'no_duplicates.csv'
output_file = 'final.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    extended_header = header + [
        'Time Posted',
        'Time Posted +30s',
        'Time Posted +5m',
        'Time Posted +15m',
        'Time Posted +1h',
        'Time Posted +4h',
        'Time Posted +24h',
        'Time Posted +1w',
        'Time Posted +30d'
      ]
    writer.writerow(extended_header)

    for row in reader:
        all_inputs = []
        original_time = int(row[3])
        times = [
            original_time,
            original_time + 30,  # +30 seconds
            original_time + 300,  # +5 minutes
            original_time + 900,  # +15 minutes
            original_time + 3600,  # +1 hour
            original_time + 14400,  # +4 hours
            original_time + 86400,  # +24 hours
            original_time + 604800,  # +1 week
            original_time + 2592000,  # +30 days
          ]
        converted_original_time = datetime.fromtimestamp(original_time)
        current_date = datetime.now()
        if converted_original_time + timedelta(days=30) > current_date:
          times.pop()

        for t in times:
            input_string = input_template.format(address=row[1], timestamp=t)
            all_inputs.append(input_string)

        # Create the full query with all inputs
        query_template = """
        query {
          getTokenPrices(
            inputs: [{inputs_placeholder}]
          ) {
            priceUsd
          }
        }
        """
        full_query = query_template.replace('{inputs_placeholder}', ', '.join(all_inputs))

        # Fetch prices and append to row
        price_data = make_api_call(full_query)

        if price_data and 'data' in price_data and 'getTokenPrices' in price_data['data']:
            for price_info in price_data['data']['getTokenPrices']:
                # Check if price_info is not None before accessing it
                if price_info is not None:
                    price = price_info.get('priceUsd', None)
                    row.append(price)
                else:
                    row.append(None)  # or some placeholder to indicate missing data
        else:
            print("API call failed or returned unexpected data.")
            # Handle cases where API response is not as expected
            # Append placeholders for each expected price data point
            for _ in range(len(times)):
                row.append(None)

        writer.writerow(row)
        time.sleep(1)


