For a while I was a member of a Telegram chat for crypto traders. I wanted to analyze the long term performance of coins mentioned by 3 of the best traders in the group (L, Rowdy, and Unipcs), so I did the following with the assistance of ChatGPT:

1. Download the chat history from Telegram
2. Extract all unique mentions of Ethereum addresses by the 3 traders (aka coin contract addresses) into a csv file
3. For each unique Ethereum address (approximately 140 of them), query the Defined API and get historical prices at the following times offset from when the address was posted in the chat

        'Time Posted',
        'Time Posted +30s',
        'Time Posted +5m',
        'Time Posted +15m',
        'Time Posted +1h',
        'Time Posted +4h',
        'Time Posted +24h',
        'Time Posted +1w',
        'Time Posted +30d'

4. Calculate the average P/L as a percentage of the original price. So for example, the average price of a coin 4 hours after being posted was +25.46%, the average price of a coin 1 week after being posted was -4.83%

here is what each individual file does. the chat history file and CSV files are in the gitignore, so you won't see them.

filter.py - extracts Ethereum addresses mentioned by the 3 traders from the Telegram chat and outputs them into output.csv

remove_duplicates.py - self explanatory, takes output.csv as the input, outputs no_duplicates.csv

caller.py - processes no_duplicates.csv, calls the defined apis for each Ethereum address in the CSV, outputs final.csv with the historical prices

defined.js - sample node script that just queries the defined api

Contact me if you have any questions or you would like to see the google document that has the final data.

test