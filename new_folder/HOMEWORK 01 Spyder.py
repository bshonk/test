# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:51:56 2017

@author: funky
"""

fruits = ['apple', 'banana', 'cherry']
for item in fruits:
    print item.upper()



hour = input("Input hours worked:")
rate = input("Input pay rate:")


total = hour * rate

print "Your wages are: ${}".format(total)


####------Bronson Notes:

def totalPay(hours, rate):
    return hours * rate
    
totalPay(10, 20)