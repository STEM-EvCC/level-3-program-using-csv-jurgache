import csv

# Specify the input and output file names
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'
incidents_data = []

# Read the CSV file and store data in a list
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    headers.append('Status')    

     # Read remaining rows
    for row in reader:
        incidents_data.append(row)
    
# Check if data was read successfully
if incidents_data:
    # Add status column with "Pending" to each row
    for row in incidents_data:
        row.append('Pending')

    # Modified data to a new csv file
    with open(output_file, 'w' , newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header
        writer.writerow(headers)

        # Write all rows
        writer.writerow(incidents_data)
    
    print(f"Successfully processed {len(incidents_data)} security incidents. ")
    print(f"Modified data saved to {output_file}")
else:
    print(f"No data found in {input_file} .")




    





