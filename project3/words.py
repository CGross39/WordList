
def num_letters(num_rows, num_columns):
    return num_rows * num_columns - (num_rows -2) *(num_columns - 2)

assert num_letters(3,4)==10
print("checking assertations.")

assert num_letters (13,4)==30
print("checking assertations")

assert num_letters (4,4)== 12
print("checking assertations")

assert num_letters (6,4)==16
print("checking assertations")

assert num_letters (6,7)==22
print ("checking assertations")

import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding='utf8')
print(data)
words=[]

rows, columns=data.shape
print(data.shape)
print(rows)
print(columns)



