"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 3:
Write a program that reads in a number and prints the either Small, Medium or Large depending on if the number is below 100 or above 200. For example, if the user enters 150 the program should display “Medium”. Another example, is if the user enters 50 the program should display “Small”. The file should be name task3.py.
"""

print("======== Number Categorize ========\n") 

number = int(input("Enter your number: "))

if number < 100 :
    print("Small")
elif number >= 100 and number <=200:
    print("Medium")
elif number > 200:
    print("Large")