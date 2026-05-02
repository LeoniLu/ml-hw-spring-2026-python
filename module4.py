""" MSCS 2202 Module4 HW
May 2, 2026
The program asks the user for input N (positive integer) and reads it

Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.
"""

def take_input():
  usr_input = input("Please enter a positive integer:\n")
  # make sure we get a positive integer
  try:
    N = int(usr_input)
    if N > 0:
      print(f"Success! You entered number {N}.\n")
      return N
    else:
      print("Invalid input, please enter a positive integer!\n")
      return take_input()
  except ValueError:
    print("Invalid input, please enter a positive integer!\n")
    return take_input()

def take_value(index):
  usr_input = input(f"Please enter int value for list element {index+1}:\n")
  try:
    value = int(usr_input)
    return value
  except:
    print("Invalid input, please enter an integer!\n")
    return take_value(index)

def insert_value(list):
  index = len(list)
  value = take_value(index);
  list.append(value)
  #print(f"The update list is: {list}")

def query_input():
  usr_input = input("Please enter an integer for query:\n")
  try:
    N = int(usr_input)
    return N
  except:
    print("Invalid, input, please enter an integer!")
    return query_input()

# prompt to ask for positive int N
N = take_input()
# construct the list db with user inputs
list = []
for i in range(N):
  insert_value(list)
print(f"The final list is {list}")
# ask for new input and return answers
input = query_input()
if input in list:
  idx = list.index(input)
  print(f"Found the input value {input} at this element {idx+1}")
  print(idx+1)
else:
  print(f"Input value {input} not in list")
  print(-1)
