# -*- coding: utf-8 -*-
"""Copy of Copy of Untitled66.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lZBJhjH0cOIfBs4lkqcJk1hDBQYaeYqR
"""

list = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    list.append(numbers)
print("Maximum element in the list is :", max(list), "\nMinimum element in the list is :", min(list))