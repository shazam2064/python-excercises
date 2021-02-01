# for i in range(5):
#     try:
#         print(i / 1)
#     except NameError:
#         print("You have a name error in your code!")

# this code here doesnt work properly #
# for i in range(5):
#     try:
#         print(i / 1)
#     except ZeroDivisionError:
#         print("Division by 0 is just wrong!")
#     print("The rest of the code...")

# for i in range(5):
#     try:
#         print(i / 1)
#     except ZeroDivisionError:
#         print("Division by 0 is just wrong!")
#     except NameError:
#         print("Name Error Detected!")
#     except ValueError:
#         print("Wrong Value!")

# this code here is not recommended #
# try:
#     print(i / 1)
# except:
#     print("Error")

# try:
#     print(4 / 2)
# except NameError:
#     print("Name Error!")
# else:
#     print("No exceptions raised by the try block!")

try:
    print(4 / 0)
except ZeroDivisionError:
    print("Not allowed")
finally:
    print("I don' care, I am getting printed either way!")
