print("Problem 1")

wordList = ["xxx", "aaa", "r5t6yy", "g", "wow"]

count = 0

for word in wordList:
    if len(word) >=2 and word[0] == word[-1]:
        count = count + 1

print(count)

print("Problem 2")

numberList = [2, 3, 5, 7, 66, 89, 134]

newList = []

userInput = int(input("Type a number here -  "))

for number in numberList:
    if (number < userInput):
        newList.append(number)

print(newList)
