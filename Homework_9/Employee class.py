import re
import datetime


class Employee:
    def __init__(self, fisrt_name, last_name, trial_passed=False):
        self.first_name = fisrt_name
        self.last_name = last_name
        self._trial_passed = trial_passed


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.split(' ')
        if len(values) != 2:
            raise ValueError('Not allowed value.')

    @property
    def phone_number(self):
        return self.phone_number

    @phone_number.setter
    def phone_number(self, _phone_number):
        def validate_phone_number(_phone_number):
            exp = (
                r'0?(77|55|99|91|98)[ -]?'
                '('
                r'(\d{3}[ -]?\d{3})|'
                r'(\d{2} \d{2} \d{2})|'
                r'(\d{2}-\d{2}-\d{2})'
                ')'
            )
            return re.fullmatch(exp, _phone_number) is not None
        if validate_phone_number(_phone_number):
            self._phone_number = _phone_number
        else:
            raise TypeError('UNSUPPORTED PHONE_NUMBER')

    @property
    def work_email(self):
        return f'{self.first_name}.{self.last_name}@company.com'.lower()

    @work_email.setter
    def work_email(self, _work_email):
        def validate_email(_work_email):
            exp = r'[a-z0-9]{1}(((\.?[\+\-\w])+[a-z0-9])?)@[a-z0-9]{1}(\.?[\+\-\w])*(\.[a-z]{2,10})'
            return re.fullmatch(exp, _work_email) is not None
        if validate_email(_work_email):
            self._work_email = _work_email
        else:
            raise TypeError('UNSUPPORTED EMAIL')

    @property
    def trial_passed(self):
        return self._trial_passed

    @trial_passed.setter
    def trial_passed(self, _trial_passed):
        if type(_trial_passed) != bool:
            raise ValueError(f'Trial_passed must be True or False, not {type(_trial_passed)}')
        else:
            self._trial_passed = _trial_passed

    @property
    def join_date(self):
        return self.join_date

    @join_date.setter
    def join_date(self, _join_date):
        d = [int(elem) for elem in _join_date.split('.')]
        self._join_date = datetime.date(d[2], d[1], d[0])

    @property
    def leave_date(self):
        return self.leave_date

    @leave_date.setter
    def leave_date(self, _leave_date):
        d = [int(elem) for elem in _leave_date.split('.')]
        self._leave_date = datetime.date(d[2], d[1], d[0])

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, _salary):
        if not (type(_salary) == int or type(_salary) == float):
            raise TypeError(f'Salary must be int or float, not {type(_salary)}')
        else:
            self._salary = _salary

    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, _gender):
        if (_gender == 'M') | (_gender == 'F'):
            self._gender = _gender
        else:
            raise TypeError("PLEASE, INPUT 'M' or 'F'")

    def __repr__(self):
        return f'Employee: {self.first_name} {self.last_name}'


emp1 = Employee('Lilit', 'Simonyan')
emp1.work_email = 'lilit.simonyan@gmail.com'
print(emp1.full_name)
# print(emp1.work_email)
# print(emp1.work_email)
emp1.join_date = '01.02.2009'
print(emp1._join_date)
# emp1.trial_passed = None
# print(emp1._trial_passed)
# emp1.phone_number = '077 34 12 04'
# print(emp1._phone_number)
# emp1.salary = 150000
# print(emp1._salary)
# emp1.gender = 'K'
# print(emp1._gender)


