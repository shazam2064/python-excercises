import psycog2

try:
    connection = psycog2.connect(database="staff", user="gabriel", pasword="python", host="127.432")

except psycog2.Error as err:
    print("An error was generated!")

else:
    print("Connection to database was successful!")

cursor = connection.cursor()

cursor.execute("select * from mystaff.employees where salary > 50000;")
