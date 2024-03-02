"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 3:
Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered. For example, if the user enters 5 10 15 -1 the program should display 30 (Each number will be separated by a carriage return). 30 is (5+10+15). The file should be named task5.py.
"""

print("======== Sum till your -1 ========\n") 

number = 0
sum = 0

while number != -1:
    number = int(input("Enter your number (type '-1' to sum): "))
    if number != -1:
        sum += number


print("Sum of all entered numbers is: ", sum)

