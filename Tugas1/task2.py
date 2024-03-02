"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 2:
Write a program that reads in a whole number and divides it by 3 and displays the result with three decimal places if they exist (rounded up). For example, if the user enters 2 the program should display 0.667. For example, if the user enters 9999 the program should display 3,333.0. The file should be name task2.py.
"""

print("======== Divided by 3 ========\n") 

number = (int(input("Enter your number: ")))

result = round(number/3, 3)

print("The result of",number,"/ 3 is:",result)
