# Handling
# Files
# with Pandas - TXT, CSV, JSON, XLSX
#
# # TXT:
# import pandas
#
# # Loading and parsing the TXT file (default delimiter is the comma) from the current directory
# dtxt = pandas.read_csv("Employees.txt")
#
# # Loading and parsing the TXT file (default delimiter is the comma) from a different directory
# dtxt = pandas.read_csv("D:\\sample_data\\Employees.txt")
#
# # Loading and parsing the TXT file using a certain delimiter
# dtxt2 = pandas.read_csv("Employees2.txt", delimiter="|")
#
# # In addition, separators longer than 1 character and different from ``'\s+'`` will be interpreted as regular expressions
# dtxt2 = pandas.read_csv("Employees2.txt", sep="|")
#
# # CSV:
# import pandas
#
# # Loading and parsing the CSV file (default delimiter is the comma) from the current directory
# dcsv = pandas.read_csv("Employees.csv")
#
# # Loading and parsing the CSV file (default delimiter is the comma) from a different directory
# dcsv = pandas.read_csv("D:\\sample_data\\Employees.csv")
#
# # Ignoring the column names in the file (on row 1) by removing the header
# dcsv = pandas.read_csv("Employees.csv", header=None)
#
# # Ignoring the column names in the file (on row 1) by removing the header and setting alternative names
# dcsv = pandas.read_csv("Employees.csv", header=None, names=["A", "B", "C", "D", "E", "F", "G", "H"])
#
# # Adding a prefix to each default column name (e.g. COL1 instead of 1)
# dcsv = pandas.read_csv("Employees.csv", header=None, prefix="COL")
#
# # Setting a column as the table index
# dcsv = pandas.read_csv("Employees.csv")
#
# # The change is made temporarily, only for the purpose of printing the table with the "ID" column as index
# dcsv.set_index("ID")
#
# # The change is made in place, meaning the DataFrame itself gets updated with the "ID" column as index
# dcsv.set_index("ID", inplace=True)
#
# # When changing the column representing the index of the table, the old column that was previously the index will be displayed to the right and it becomes a regular column in the table
# dcsv.set_index("Address", inplace=True)
#
# # Finding out the shape (no of rows and columns) of a table (DataFrame)
# dcsv.shape
#
# # Line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file.
# dcsv = pandas.read_csv("Employees.csv", skiprows=4)
#
# # Number of rows of file to read. Useful for reading pieces of large files
# dcsv = pandas.read_csv("Employees.csv", nrows=5)
#
# # Getting all the available optional parameters of the read_csv() method
# help(pandas.read_csv)
#
# # JSON:
# import pandas
#
# # Loading a JSON file from the current directory
# djson = pandas.read_json("Employees.json")
#
# # Loading a JSON file from a different directory
# djson = pandas.read_json("D:\\sample_data\\Employees.json")
#
# # XLSX:
# import pandas
#
# # Installing the xlrd module in the Windows cmd
# pip
# install
# xlrd
#
# # Loading an Excel file from the current directory
# dxlsx = pandas.read_excel("Employees.xlsx")
#
# # Loading an Excel file from a different directory
# dxlsx = pandas.read_excel("D:\\sample_data\\Employees.xlsx")
#
# # Loading a certain sheet from an Excel file, by its index (first sheet is index 0)
# dxlsx = pandas.read_excel("Employees.xlsx", sheet_name=0)
#
# More
# info:
# https: // pandas.pydata.org / pandas - docs / stable / user_guide / io.html