def reverse_palindrome(palindrome):
    if not palindrome:
        return ""
    return reverse_palindrome(palindrome[1:]) + palindrome[0]

def is_palindrome(palindrome):
    if reverse_palindrome(palindrome) == palindrome:
        return "YES"
    return "NO"

text = input('Enter a text: ')
print(is_palindrome(text))