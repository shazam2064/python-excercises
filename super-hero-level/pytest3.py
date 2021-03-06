import math
import pandas


# Defining the function with 3 parameter
def calculator(excel_path, price_index):
    # Loading the excel (D:\\testing\\values.xlsx) values into a Pandas Dataframe
    df = pandas.read_excel(excel_path)

    # The value of x
    x = float(df["Price"][price_index])

    # The value of x
    y = float(input("Enter te value of y: "))

    # The final result
    result = round(math.pow(x / y, 2))

    # Returning the result
    return result

# calculator("D:\\testing\\values.xlsx", 0)

# End of program
