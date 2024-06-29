from pprint import pprint

file_name = 'test.txt'
file_open = open(file_name, 'r')
pprint(file_open.read())
file_open.close()