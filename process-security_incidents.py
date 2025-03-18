import csv

# Specify the input and output file names
input_file = 'security_incidents.csv'
output_file = 'security_incidents_modified.csv'
incidents_data = []

# Read the CSV file and store data in a list
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # header row and add Status
    headers = next(reader) + ['Status']

     # Read each row and append to data list
    for row in reader:
        incidents_data.append(row)
    
    # Status coloumn with default value Pending to each row
    modified_data = []
    for row in incidents_data:
        modified_row = row + ['Pending']
        modified_data.append(row)

    # Modified data to a new csv file
    with open(output_file, 'w' , newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header
        writer.writerow(headers)

        # Write all rows
        writer.writerow(modified_data)
    
    print(f"Successfully processed {len(incidents_data)} security incidents. ")
    print(f"Modified data saved to {output_file}")




    





