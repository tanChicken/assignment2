import pandas as pd
from datetime import datetime

# Function to convert date format
def convert_date_format(date_str):
    # Convert the date string into a datetime object
    date_obj = datetime.strptime(date_str, '%d-%b-%y')
    # Format the date into "Jan 1 2000" without leading zero
    return date_obj.strftime('%b %e %Y').strip()

# Read data from CSV file
input_file = 'clean_exchange_rate_new.csv'  # Update this path to your input CSV file
df = pd.read_csv(input_file)

# Apply the date conversion function to the 'date' column
df['date'] = df['date'].apply(convert_date_format)

# Save the modified DataFrame to a new CSV file
output_file = 'clean_exchange_rate_new.csv'  # Update this path for your output CSV file
df.to_csv(output_file, index=False)

print(f"Date format conversion completed. The updated file is saved as '{output_file}'.")
