# -*- coding: utf-8 -*-
"""DLBCL_FL_without _module.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u7Pe455sPetRgMA3W4cA1RWnOiRQafbD
"""

file_dir = '/content/drive/MyDrive/test_data/dlbcl-fl.csv'

"""# Reading the CSV"""

def read_csv(file_dir):
    f = open(file_dir, 'r')
    list_data = f.readlines()
    for line in list_data:
        f.close()
        yield line

"""# Printing the data"""

def print_csv(file_dir):
    for line in read_csv(file_dir):
        print([line.replace('\n','')])

print_csv(file_dir)

"""# Counting the number of rows in CSV"""

def row_count(file_dir):
    count = 0
    for row in read_csv(file_dir):
        count = count + 1
    return count

row_count(file_dir)

"""# Counting the number of columns"""

def column_count(file_dir):
    for f_row in read_csv(file_dir):
        ncol = f_row.count(',') + 1
        return ncol
     
column_count(file_dir)

"""# Printing the first row of CSV"""

def print_first_row_of_csv(file_dir):
    for first_row in read_csv(file_dir):
        print([first_row])
        break

print_first_row_of_csv(file_dir)

"""# Printing the CSV without the first row"""

def print_without_1_row(file_dir):
    flag = False
    for row in read_csv(file_dir):
        if bool(flag) == False:
            flag = True
            pass
        else:
            print([row.replace('\n', '')])

print_without_1_row(file_dir)

"""# Printing the last column of CSV """

def print_last_col(file_dir):
    with open(file_dir, 'r') as csv:
        data = [line.replace('\n','').split(',')[-1] for line in csv.readlines()]
        return data

print_last_col(file_dir)

"""# Printing the data without column Labels and target class"""

def only_data(file_dir):
    flag = False
    for row in read_csv(file_dir):
        if bool(flag) == False:
            flag = True
            pass
        else:
            l = row.strip().split(',')[-1]
            row = row.replace(l, "")
            print([row])

only_data(file_dir)

"""# Printing Unique class labels

"""

list_data = print_last_col(file_dir)

def unique_class_labels(list_data):
    unique_list = []

    for x in list_data: 
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        print(list(x.split(',')))

unique_class_labels(list_data)