# from utils import file_operations
#
# file_operations.save_to_file('Rolf', 'data.txt')
# print(file_operations.read_from_file('data.txt'))

'''
We're getting into Foley territory!
While that may be harder to read, it's useful to prevent duplicate-named functions.
Iif you don't have many functions to import
and if they are uniquely named,
you can use:
'''
from utils.file_operations import save_to_file, read_from_file

save_to_file('Rolf', 'data.txt')
print(read_from_file('data.txt'))
