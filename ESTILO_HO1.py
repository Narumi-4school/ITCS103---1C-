


word = input("Enter a word: ")
num_list = []
word_len = len(word)
 # Tried the basic way of appending in the list 
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)
num_list.append(num6)
print(f"The length of the word is {len(word)}") # Prints the length of the word
print(num_list)

sum = num1 + num2 + num3 + num4 + num5 + num6 
aver = sum / 6                                  
print(f"The average of all typed number is {aver}") # Prints the average of all numbers in the list
  
  # Checks the length of the word with the average of listed numbers
if aver > word_len:
    print(f"The length of the word {word} is less than the average.")
elif aver == word_len:
    print(f"The length of the word {word} is equal to the average.")
else:
    print(f"The length of the word {word} is greater than the average.")        
 