import csv

def update_csv_cell(csv_file, row_index, col_name, new_value):
    # Read the CSV file into a list of dictionaries
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        header = reader.fieldnames
        indeex = header.index("Name")
        print(header[indeex])
        print(header)
        uind = None
        for index,val in  enumerate(data):
            # print(index)
            if int(val['Student Id']) == 21049919:
                uind = index
                print(val['Name']) 
        print(uind)

    # Update the value at the specified cell
    # data[row_index][col_name] = new_value

    # # Write the updated data back to the CSV file
    # fieldnames = reader.fieldnames
    # with open(csv_file, 'w', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(data)

# Example usage
csv_file_path = 'example.csv'
row_to_update = 1  # Index of the row (0-based)
column_to_update = 'Name'  # Name of the column to update
new_cell_value = 'Kabin'

update_csv_cell(csv_file_path, row_to_update, column_to_update, new_cell_value)
