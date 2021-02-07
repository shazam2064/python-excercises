# Iterators - an object which allows a programmer to traverse through all the elements of a collection
my_list = [1, 2, 3, 4, 5, 6, 7]

my_iter = iter(my_list)  # iter() returns an interator object

next(
    my_iter)  # in Python 2 and 3, it returns the elements of a sequence one by one; raises StopIteration when the sequence is exhausted


# Generators - special routines that can be used to control the iteration behavior of a loop; defined using the "def" keyword;
def my_gen(x, y):  # creating a generator function
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y  # yields the values one at a time; traversing a sequence up to a certain point, getting the result and suspending the execution


my_object = my_gen(10, 5)  # creating a generator object

next(
    my_object)  # manually yield the next element returned by the my_gen() function; raises StopIteration when the sequence is exhausted

gen_exp = (x for x in range(
    5))  # creating a generator expression; similar to list comprehensions, but using parentheses instead of square brackets

next(
    gen_exp)  # extracting each value in the list generated by range(5), one value at a time; raises StopIteration when the sequence is exhausted
