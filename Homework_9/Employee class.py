import re
import datetime


class Employee:
    def __init__(self, fisrt_name, last_name, trial_passed=False, gender='M'):
        self.first_name = fisrt_name
        self.last_name = last_name
        self.trial_passed = trial_passed
        self.gender = gender

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.split(' ')
        if len(values) != 2:
            raise ValueError('Not allowed value.')

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, phone_number):
        def validate_phone_number(phone_number):
            exp = (
                r'0?(77|55|99|91|98)[ -]?'  # operator code
                '('
                r'(\d{3}[ -]?\d{3})|'  # version 1
                r'(\d{2} \d{2} \d{2})|'  # version 2
                r'(\d{2}-\d{2}-\d{2})'  # version 3
                ')'
            )
            return re.fullmatch(exp, phone_number) is not None
        if validate_phone_number(phone_number):
            self.phone_number = phone_number
        else:
            raise TypeError('UNSUPPORTED PHONE_NUMBER')  # էլ. հասցեի դեպքում ստուգումն անում է, այս դեպքում՝ ոչ

    @property
    def work_email(self):
        return f'{self.first_name}.{self.last_name}@company.com'.lower()

    @work_email.setter
    def work_email(self, email):
        def validate_email(email):
            exp = r'[a-z0-9]{1}(((\.?[\+\-\w])+[a-z0-9])?)@[a-z0-9]{1}(\.?[\+\-\w])*(\.[a-z]{2,10})'
            return re.fullmatch(exp, email) is not None
        if validate_email(email):
            self.email = email
        else:
            raise TypeError('UNSUPPORTED EMAIL')

    @property
    def start_date(self):
        return self.start_date

    @start_date.setter
    def start_date(self, join_date):
        d = [int(elem) for elem in join_date.split('.')]
        self.join_date = datetime.date(d[2], d[1], d[0])

    @property
    def end_date(self):
        return self.end_date

    @end_date.setter
    def end_date(self, leave_date):
        d = [int(elem) for elem in leave_date.split('.')]
        self.leave_date = datetime.date(d[2], d[1], d[0])

    @property
    def salary_func(self):
        return self.salary_func

    @salary_func.setter
    def salary_func(self, salary):
        self.salary = salary

    def __repr__(self):
        return f'Beneficiary: {self.first_name} {self.last_name}'




