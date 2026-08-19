'''Given the string variable:word = "PythonProgramming"
Write Python code to slice and print:  
The first 6 characters ("Python").  
The word "Program" using positive indices.  
The last 3 characters ("ing") using negative indices.  '''

word = "PythonProgramming"
print(f"First 6 characters: {word[0:6]}")
print(f"The word Program: {word[6:13]}")
print(f"The last 3 characters: {word[-3:]}")

