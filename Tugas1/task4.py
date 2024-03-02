"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 3:
Write a program that reads in a number and prints the sum of all values from 1 up to the number. For example, if the user enters 5 the program should display 15. 15 is (1+2+3+4+5). The file should be named task4.py.
"""

print("======== Sum till your number ========\n") 

number = int(input("Enter your number: "))

sum = 0
for i in range(1, number + 1):
    sum += i

print("Sum of all values from 1 till your number",number,"is:", sum)