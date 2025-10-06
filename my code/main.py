import numpy as np

data = np.genfromtxt("A:\data.csv", delimiter=',', dtype=str, skip_header=1)

name = data[:, 0]
age = data[:, 1].astype(int)
salaries = data[:, 2].astype(int)

print ('All names:', name)
print ('All ages:', age)
print ('All salaries:', salaries)

print ('\n Average Salaries:', np.mean(salaries))
print ('\n Highest Salaries:', np.max(salaries))
print ('Lowest Salaries:', np.min(salaries))

highest_salaries_index = np.argmax(salaries)
print ('Richest Person:', name[highest_salaries_index])
