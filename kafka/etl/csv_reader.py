import csv


class CsvReader:
    def read_csv(self, csv_file='../../resources/employees.csv'):
        with open(csv_file, newline='') as csvfile:
            rows = []
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in spamreader:
                print(', '.join(row))
                rows.append(row)
            return rows
