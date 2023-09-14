#Write a python script to enter any number and check its prime or not.
print("Program to check number is prime or not)")
n=int(input("Enter the Number: "))
if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			print(n, "is not a prime number")
		break
	else:
		print(n, "is a prime number")
else:
	print(n, "is not a prime number")

#Write a python script to enter any number and print the sum of its digit.
print("\npython script to enter any number and print the sum of its digit.")
n=input("Enter the Number: ")
sum=0
for i in n:
    sum=sum+int(i)
print("Sum Of Given Number Is: ",sum)



#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
print("\nprogram to check Enter the Number It Is Palindrom Or Not:")
n=input("Enter the Number To Check It Is Palindrom Or Not: ")
if n==n[::-1]:
    print(n,"Is Palindrom Number")
else:
    print(n,"Is Not palindrom Number")



#Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.
print("\nprogram to check Enter the Number It Is armstrong Or Not:")
num = int(input("Enter a number: "))
sum = 0
n1 = len(str(num))
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n1
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



#Write a python script to enter any string and count vowel.
print("\npython script to enter any string and count vowel.")
str=input("Enter String: ")
count_vowel=0
vowel=['a','e','i','o','u','A','E','I','O','U']
for i in str:
    if i in vowel:
        count_vowel+=1
print("Available Vowel In String Is: ",count_vowel)



#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
print("\nWrite a python script to enter any string and print only part of string. Take input of start character and end character from user.")
string_input=input(("Enter The String: "))
first_input=input(("Enter The First Character: "))
last_input=input(("Enter The Last Character: "))

start_index=string_input.find(first_input)
end_index=string_input.find(last_input)

if start_index==-1:
    print("Start Character Is Not Found")
    exit()

if end_index==-1:
    print("End Character Is Not Found")
    exit()

if end_index<start_index:
    print("End Character Cannot be Before Start Character")
    exit()

print("Result: ",string_input[start_index:end_index+1])


#Write a python script to enter any string, replace vowel with its position number.
print("\nWrite a python script to enter any string, replace vowel with its position number.")
string_input=input(("Enter The String: "))
vowels='aeiouAEIOU'
result=''
position=1
for char in string_input:
    if char in vowels:
        result+=str(position)
        position+=1
    else:
        result+=char

print(result)

