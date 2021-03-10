class Pensioner:
    B = 18000  # amount of the basic pension

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, full_name):
        values = full_name.split(' ')
        if len(values) != 2:
            raise ValueError('Not allowed value.')

    @property
    def experience(self):
        return self.experience

    @experience.setter
    def experience(self, _experience):
        if _experience > 10:
            self._experience = _experience
        else:
            raise TypeError('NOT ENOUGH EXPERIENCE FOR PENSION')

    @property
    def coye(self):  # the cost of one year of work experience
        if 10 <= self._experience:
            return 500
        else:
            raise TypeError('NOT ENOUGH EXPERIENCE FOR PENSION')

    @property
    def coefficient(self):  # Retiree personal ratio
        if 11 <= self._experience <= 40:
            return 1 + (self._experience - 10) * 0.01
        elif 41 <= self._experience:
            return 1.3 + (self._experience - 40) * 0.02
        else:
            raise TypeError('NOT ENOUGH EXPERIENCE FOR PENSION')

    @property
    def pension_amount(self):
        return round(Pensioner.B + (9500 + (self._experience - 10) * self.coye) * self.coefficient)

    @staticmethod
    def pension_formula():
        return 'pension = basic + (9500 + (experience -10) * cost_of_one_year_experience) * coefficient'


class DisabilityEmploymentPension1(Pensioner):  # first group Disability
    def __init__(self, first_name, last_name, group_type=1):
        super(DisabilityEmploymentPension1, self).__init__(first_name, last_name)
        self.group_type = group_type

    @property
    def pension_amount(self):
        return round((Pensioner.B + (9500 + (self._experience - 10) * self.coye) * self.coefficient)+7200)


class DisabilityEmploymentPension2(Pensioner):  # second group Disability
    def __init__(self, first_name, last_name,group_type=2):
        super(DisabilityEmploymentPension2, self).__init__(first_name, last_name)
        self.group_type = group_type

    @property
    def pension_amount(self):
        return round((Pensioner.B + (9500 + (self._experience - 10) * self.coye) * self.coefficient)+3600)


class DisabilityEmploymentPension3(Pensioner): # first group
    def __init__(self, first_name, last_name, __person_id=None, psn=None, group_type=3):
        super(DisabilityEmploymentPension3, self).__init__(first_name, last_name)
        self.group_type = group_type

p1 = Pensioner("Tigran", "Simonyan")
p1.experience = 45
print(f'Pensioner: {p1.full_name} Experience: {p1._experience}')
# print(p1.coefficient)
print(f'Pension amount: {p1.pension_amount}')
p2 = DisabilityEmploymentPension1("Poghos", "Poghosyan")
p2.experience = 45
print(f'Pensioner: {p2.full_name} Experience: {p2._experience} Disability group: {p2.group_type}')
# print(p2.coefficient)
print(f'Pension amount: {p2.pension_amount}')
p3 = DisabilityEmploymentPension2("Petros", "Petrosyan")
p3.experience = 45
print(f'Pensioner: {p3.full_name} Experience: {p3._experience} Disability group: {p3.group_type}')
# print(p2.coefficient)
print(f'Pension amount: {p3.pension_amount}')
print(Pensioner.pension_formula)

