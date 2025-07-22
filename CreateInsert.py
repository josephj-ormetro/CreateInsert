import csv 
import pyperclip
import argparse

# Create an argument parser to take in table name and file name
parser = argparse.ArgumentParser(
    description = "Accepts a csv data file and a table name, creates an  \
        insert statement of the csv data into the table, and copies the  \
        statement into your clipboard"
)

parser.add_argument('tablename', type=str,
                   help='Name of destination table to insert into')
parser.add_argument('datafile', type=str,
                   help='csv file containing data to insert')
args = parser.parse_args()
datafile = args.datafile
tablename = args.tablename

# Get all the rows of the CSV file
rows = []
try:
    with open(datafile) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows += [row]
except FileNotFoundError:
    print(f"Error - file {datafile} was not found")
except Exception as e:
    print(f"An error occured: {e}")


# Helper that returns numeric (decimal) values without single quotes
# and returns everything else surrounded by single quotes for SQL
# insert statement
def formatValue(stringValue):
    try:
        float(stringValue)
        return stringValue
    except ValueError:
        return f"\'{stringValue}\'"
    

# Turns each csv row into a string in format (value, value value)
asStrings = []
for i in range(len(rows)):
    row = rows[i]
    # Start a new value row
    thisRow = '\t('
    for j in range(len(row)):
        # append each value to the string, formatting types accordingly
        value = row[j]
        # if it's the first row of the spreadsheet, don't quote - these
        # are column names
        if i == 0:
            thisRow += value
        # otherwise, quote anything that's not a number (including dates)
        else:
            thisRow += formatValue(value)
        if j < len(row) - 1:
            thisRow += ',\t'
    
    # end the row. If it's not the first or last row, add a comma and newline
    thisRow += ')'
    if i > 0 and i < len(rows) - 1:
        thisRow += ',\n'
    asStrings.append(thisRow)

# The first value row should actually be column names
columnNames = asStrings[0]
# The rest are the actual values to insert
valuesStatement = asStrings[1:]

buildString = f'INSERT INTO {tablename}\n{columnNames}\nVALUES\n'
for values in valuesStatement:
    buildString += values
buildString += ';'
print(buildString)

# Copy to clipboard
pyperclip.copy(buildString)