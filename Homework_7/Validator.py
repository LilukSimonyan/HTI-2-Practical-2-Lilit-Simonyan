import re

def validate_phone_number(identifier1):

    expression = '^('\
                    '([0]?[5][5])|'\
                        '([0]?[7][7])|'\
                            '([0]?[9][189]))'\
                                '(([\ ]?)([0-9]{6}$)|'\
                                    '(([\ ])([0-9]{2}[-][0-9]{2}[-][0-9]{2}$))|'\
                                        '(([-])([0-9]{2}[-][0-9]{2}[-][0-9]{2}$))|'\
                                            '(([\ ])([0-9]{2}[\ ][0-9]{2}[\ ][0-9]{2}$))|'\
                                                '(([-])([0-9]{3}[-][0-9]{3}$))|'\
                                                    '(([\ ])([0-9]{3}[\ -][0-9]{3}$))'\
                 ')'

    if re.fullmatch(expression, identifier1):
        return True
    return False

def validate_email(identifier2):
    expression = '(^[a-zA-Z0-9][a-z0-9+-\.]{1,64}@([\w-]+\.)+[\w-]{2,6}$)'

    if re.fullmatch(expression, identifier2):
        return True
    return False

def validator(n):
    if n[0:5] == 'email':
        if len(n) < 6:
            return 'No value passed.'
        elif validate_email(n[7:len(n)-1]):
            return 'Yes'
        return 'No'
    elif n[0:12] == 'phone_number':
        if len(n) < 13:
            return 'No value passed.'
        if validate_phone_number(n[14:len(n)-1]):
            return 'Yes'
        return 'No'
    else:
        return 'No such command.'

validation = input('Enter <validation_method>, then "<the value that needs to be validated>": ')
print(validator(validation))

