import csv

class CSVOpener:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        try:
            with open(self.filepath, mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file {self.filepath} does not exist.")
            return None
        


csv_file = CSVOpener("testfile.csv")

data = csv_file.read()

print(data)


#arek nykiel paweł milczarek