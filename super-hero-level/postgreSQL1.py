# # Show databases
# \l
#
# # Create database
# create
# database
# staff;
#
# # Connect to a database
# \c
# staff;
#
# # Create a new user with a password
# create
# user
# mihai
# with encrypted password 'python';
#
# # Show users
# \du
#
# # Grant privileges on a database to a user
# grant
# all
# privileges
# on
# database
# staff
# to
# mihai;
#
# # Create a new schema
# create
# schema
# mystaff
# authorization
# john;
#
# # Show schemas
# \dn
#
# # Deleting a schema / database / user
# drop
# schema
# mystaff;
# \c
# postgres
# drop
# database
# staff;
# drop
# user
# mihai;