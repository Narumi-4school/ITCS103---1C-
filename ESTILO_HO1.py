word = input("Enter a word: ")
word_len = len(word)
num_list = []

for i in range(1,word_len):
  num_choice = eval(input(f"Enter number{i}: "))
  num_list.append(num_choice)
  
print(f"The length of the word {word} is {word_len}.")
print(num_list)

aver = sum(num_list) / len(num_list)
print(f"The average of all numbers is {aver}")

if word_len > aver:
  print(f"The length of the word {word} is greater than the average.")
elif word_len < aver:
  print(f"The length of the word {word} is less than the average.")
else:
  print(f"The length of the word {word} is equal to the average.")