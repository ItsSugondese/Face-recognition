import csv
import os

# Data to be written to the CSV file
class MakeIt:
    
    def __init__(self):
        self.fileName = 'example.csv'
        pass

    def makeCSV(self, id, name):
        data = {'Student Id' : id, 'Name' : name, 'Verified' : False}
        fieldnames = ['Student Id', 'Name', 'Verified']

        if os.path.exists(self.fileName):
            with open(self.fileName, 'r') as file:
                csv_reader = csv.DictReader(file)
                
                for row in csv_reader:
                    if int(row['Student Id']) == id:
                        return "Student with that id already exists"
        

        with open(self.fileName, 'a', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=data.keys())
        # If the file is empty, write the header
            if file.tell() == 0:
                csv_writer.writeheader()
        # Write the data
            csv_writer.writerow(data)
            return "CSV saved successfully"

        return ""

    def updateCSV(self, id):
        with open(self.fileName, 'r') as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            data = list(reader)
            rowIndex = None
            colIndex = None
            for index,val in  enumerate(data):
                if(int(val['Student Id']) == id):
                    rowIndex = index
                    colIndex = headers[headers.index("Verified")]
                
        # Update the value at the specified cell
            data[rowIndex][colIndex] = True

        # Write the updated data back to the CSV file
            fieldnames = reader.fieldnames
            with open(self.fileName, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

    def getStudentNameFromCSV(self, id):
        with open(self.fileName, 'r') as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                data = list(reader)
                rowIndex = None
                colIndex = None
                for index,val in  enumerate(data):
                    if int(val['Student Id']) == int(id):
                        colIndex = headers[headers.index("Name")]
                        print(f"column index is {colIndex}")
                        return val["Name"]