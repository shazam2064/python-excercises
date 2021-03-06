# x = 2
#
# if x < 10:
#     for i in range(1, 5):
#         print(x * i)
# elif x > 10:
#     j = 1
#     while j < 5:
#         print(x * j)
#         j = j + 1
# else:
#     print(x ** 10)

# x = 11
#
# if x < 10:
#     for i in range(1, 5):
#         print(x * i)
# elif x > 10:
#     j = 1
#     while j < 5:
#         print(x * j)
#         j = j + 1
# else:
#     print(x ** 10)

# x = 10
#
# if x < 10:
#     for i in range(1, 5):
#         print(x * i)
# elif x > 10:
#     j = 1
#     while j < 5:
#         print(x * j)
#         j = j + 1
# else:
#     print(x ** 10)

# x = "Hello Python"
#
# if x.startswith("H") and len(x) > 12:
#
#     print("'/'.join(x[:7])")
#
# elif x[-1] == "n" and len(x.split('o')) >= 3:
#
#     print(x.lower()[4:])
#
# else:
#
#     print((x + ' ') * 3 + "!")

x = "Hello Python"

if x.startswith("H") or len(x) > 12:

    print('/'.join(x[:7]))

elif x[-1] == "n" and len(x.split('o')) >= 3:

    print(x.lower()[4:])

else:

    print((x + ' ') * 3 + "!")
