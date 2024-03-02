"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 1:
Write a program using Python that reads in the user's salary and divides the number by 12 months. The monthly salary should be output to the console with 0 decimal places rounded up. For example, if the user enters 60000 the program should display 5000. The file should be name task1.py.
"""

print("======== Salary ========\n") 

salary = (float(input("Enter your yearly salary: ")))

monthlySalary = int(salary / 12)

print("Your monthly Salary is:", monthlySalary)



