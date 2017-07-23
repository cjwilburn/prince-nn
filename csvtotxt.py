# import libraries

import csv

csv_file = raw_input('Enter the name of your input file: ')
txt_file = raw_input('Enter the name of your output file: ')

text_list = []

with open(csv_file, "r") as my_input_file:
    for line in my_input_file:
        line = line.split(",", 2)
        text_list.append(" ".join(line))

with open(txt_file, "w") as my_output_file:
    my_output_file.write("#1\n")
    my_output_file.write("double({},{})\n".format(len(text_list), 2))
    for line in text_list:
        my_output_file.write("  " + line)
    print('File Successfully written.')
