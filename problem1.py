s = input("Enter a string: ")
string1=""
string2=""
string3=""
string4=""
for alphabet in s:
    if alphabet.isupper():
        string1 += alphabet
    elif alphabet.islower():
        string2 += alphabet
    elif alphabet.isdigit():
        string3 += alphabet
    elif not alphabet.isalnum():
        string4 += alphabet

print(string1)
print(string2)
print(string3)
print(string4)