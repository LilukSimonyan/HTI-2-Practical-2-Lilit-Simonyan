def is_palindrome(input_text):
    if not input_text:
        return "YES"
    if input_text[0] == input_text[-1]:
        return is_palindrome(input_text[1:len(input_text) - 1])
    else:
        return "NO"

text = input('Enter a text: ')
print(is_palindrome(text))
