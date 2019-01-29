import requests


class Staff:
    """A sample Staff class"""

    raise_incent = 1.15

    def __init__(self, first, last, sal):
        self.firstname = first
        self.lastname = last
        self.salary = sal

    @property
    def email(self):
        return '{}.{}@mycompany.com'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_incentive(self):
        self.salary = int(self.salary * self.raise_incent)

    def yearly_report(self, year):
        response = requests.get(f'http://mycompany.com/{self.lastname}/{year}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'