#Calculate Execution Time in Python Code

# So to calculate the execution time of a python program, we need to Follow these steps  mentioned below.
# 1. First, Store the initation of the Program into a variable
# 2. Write the python program
# 3. Store the end time of the program into a variable 
# 4. Subtract the time of initiation of the program from the end time of the program 
# In the end you  will get the execution time of your program in seconds

from time import time

start = time()

# Python program to create Acronyms

word = "Artificial Intellgence"
text = word.split()

a = " "

for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()

execution_time = end - start

print("Execution Time: ",execution_time)