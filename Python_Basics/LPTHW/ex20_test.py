from sys import argv
script, file_to_open = argv

current_file =  open(file_to_open)
print current_file.readline()
print current_file.readline()
print current_file.readline()
current_file.close()
