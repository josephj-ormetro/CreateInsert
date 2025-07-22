# CreateInsert
command line utility to turn a csv file into a SQL insert statement

## Build
1. Run:
```
pip install -r requirements.txt` to install dependencies
```
2. Run: 
```
pyinstaller -F CreateInsert.py
```
This will create some files and directories. In the `dist` folder that gets created, there will be a `CreateInsert.exe` file.
3. Copy the `CreateInsert.exe` file somewhere that's in your system or user path

## Use

usage: CreateInsert.exe [-h] tablename datafile

Accepts a csv data file and a table name, creates an " insert statement of the csv data into the table, and copies the " statement into your clipboard

positional arguments:
  tablename   Name of destination table to insert into
  datafile    csv file containing data to insert

options:
  -h, --help  show this help message and exit