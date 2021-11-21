# Write your code here :-)
message = 'Hello Precious!, how are you doing? I want to tell you that I am doing just fine.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
