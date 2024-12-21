######### 1 Question #########

a = 0
b = 1
print("fibonacci 0 to 50: ")
for i in range(50):
    if a > 50:
        break
    print(a, end=" ")
    a,b=b,a+b

###### 2nd Question ########

word = input("Enter a word: ")
word = word.lower()

if word == word[::-1]:
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")

n = input('enter a word: ')
reversed = n[::-1]
print(reversed)




