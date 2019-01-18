import matplotlib.pyplot as plt
import numpy as np
import csv

A = []
B = []
years_list = []
salary_list = []
with open('Salary_Data.csv', 'r') as f:
    lines = csv.reader(f)
    for line in lines:
        try:
            years_list.append(float(line[0]))
            salary_list.append(float(line[1]))
        except ValueError:
            years_list.append(line[0])
            salary_list.append(line[1])
        A.append([line[0], 1])
        B.append([line[1]])

A = np.array(A[1:], dtype='float64')
A = np.mat(A)
B = np.array(B[1:], dtype='float64')
B = np.mat(B)
A_T = A.T

cal_A = A_T * A
cal_B = A_T * B
cal_A_inverse = np.linalg.pinv(cal_A)
X = cal_A_inverse * cal_B

X = X.tolist()

s = []
x = np.linspace(start=1, stop=12, num=100)
y = x*X[0][0]+X[1][0]
years_list = years_list[1:]
salary_list = salary_list[1:]
plt.figure()
plt.plot(x, y, linestyle='--', color='red')
plt.plot(years_list, salary_list, 'ob', )
plt.xlim((1, 15))
plt.ylim((1000, 200000))
plt.xlabel('Years Experience  (year)')
plt.ylabel('Salary  (RMB)')
plt.annotate('y = {k} * x + {b}'.format(k=X[0][0], b=X[1][0]), xy=(5, 180000))
plt.savefig('salary-yearsExperience.jpg')
plt.show()


