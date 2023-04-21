
# import packages
import pandas as pd
import time

# set input and output csv paths
input_file = "input.csv"
output_file = "output.csv"

# infinite loop to run until not needed

while True:
    # Read input CSV file
    df = pd.read_csv(input_file)

    # Write from dataframe to output file
    df.to_csv(output_file, index=False)
    print(f"Data saved to file: {output_file}")

    # Wait for one second
    time.sleep(1)
