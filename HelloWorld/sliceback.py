letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1] # python idiom to reverse a sequence
print(backwards)

# create a slice that produces the characters qpo
print(letters[-10:-13:-1]) # print(letters[16:13:-1])

# slice the string to produce edcba
print(letters[-22::-1]) # print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[-1:-9:-1]) # print(letters[:-9:-

print(letters[-4:]) # to get the last characters of a sequence
print(letters[-1:])
print(letters[:1]) # to get the first character of a sequence
