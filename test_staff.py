import unittest
from unittest.mock import patch
from staff import Staff


class TestStaff(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.empNo1 = Staff('Andrew', 'Marray', 50000)
        self.empNo2 = Staff('Julian', 'Porres', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.empNo1.email, 'Andrew.Marray@mycompany.com')
        self.assertEqual(self.empNo2.email, 'Julian.Porres@mycompany.com')

        self.empNo1.firstname = 'John'
        self.empNo2.firstname = 'Jane'

        self.assertEqual(self.empNo1.email, 'John.Marray@mycompany.com')
        self.assertEqual(self.empNo2.email, 'Jane.Porres@mycompany.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.empNo1.fullname, 'Andrew Marray')
        self.assertEqual(self.empNo2.fullname, 'Julian Porres')

        self.empNo1.firstname = 'John'
        self.empNo2.firstname = 'Jane'

        self.assertEqual(self.empNo1.fullname, 'John Marray')
        self.assertEqual(self.empNo2.fullname, 'Jane Porres')

    def test_apply_incentive(self):
        print('test_apply_incentive')
        self.empNo1.apply_incentive()
        self.empNo2.apply_incentive()

        self.assertEqual(self.empNo1.salary, 57499)
        self.assertEqual(self.empNo2.salary, 69000)

    def test_yearly_report(self):
        with patch('staff.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.empNo1.yearly_report('2017')
            mocked_get.assert_called_with('http://mycompany.com/Marray/2017')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.empNo2.yearly_report('2018')
            mocked_get.assert_called_with('http://mycompany.com/Porres/2018')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
        unittest.main()