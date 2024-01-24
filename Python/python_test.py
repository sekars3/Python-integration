def reverse_string(word):
    rev_word = ""
    len_word = len(word)
    for i in range(0,len_word):
        rev_word += word[len_word-1-i]
    return rev_word
    
def reverse_num(num):
    temp_num = num
    rev_num = 0
    reminder = temp_num%10
    while(reminder != 0):
        rev_num = rev_num*10 + reminder
        temp_num = temp_num//10
        reminder = temp_num%10
    return rev_num
