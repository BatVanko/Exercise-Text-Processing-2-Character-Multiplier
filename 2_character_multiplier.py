text_line = input().split(" ")
first_word = text_line[0]
second_word = text_line[1]
total_sum = 0
if len(first_word) == len(second_word):
    for i in range(len(first_word)):
        result = ord(first_word[i]) * ord(second_word[i])
        total_sum += result
elif len(first_word) > len(second_word):
    for i in range(len(first_word)):
        if i < len(second_word):
            result = ord(first_word[i]) * ord(second_word[i])
            total_sum += result
        else:
            total_sum += ord(first_word[i])
elif len(first_word) < len(second_word):
    for i in range(len(second_word)):
        if i < len(first_word):
            result = ord(first_word[i]) * ord(second_word[i])
            total_sum += result
        else:
            total_sum += ord(second_word[i])

print(total_sum)









