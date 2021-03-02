"""Crimetime test file
CPE 101
Spring 2020
Author: Brenden Rogers
"""

import crimetime
import unittest


class MyTest(unittest.TestCase):
    """To test crimetime files"""
    def test_create_crimes(self):
        # c_1 = ['13456', 'ROBBERY', 'BODILY FORCE']
        # c_2 = ['13456', 'ROBBERY', 'ARMED ROBBERY']
        # c_3 = ['23145', 'THEFT', 'LOOTING']
        # c_4 = ['98635', 'MURDER', 'STABBING']
        # c_5 = ['54313', 'ROBBERY', 'BODILY FORCE']
        # c_6 = ['63527', 'VANDALISM', 'GRAFFITI']
        # c_7 = ['72514', 'ROBBERY', 'ARMED']
        # crime_lines = [c_1, c_2, c_3, c_4, c_5, c_6, c_7]
        # rob_1 = crimetime.Crime('13456', 'ROBBERY')
        # rob_2 = crimetime.Crime('54313', 'ROBBERY')
        # rob_3 = crimetime.Crime('72514', 'ROBBERY')
        # lst_of_crime = [rob_1, rob_2, rob_3]
        # test_val = crimetime.create_crimes(crime_lines)
        # expected_val = lst_of_crime
        # self.assertEqual(test_val, expected_val)
        c_1 = ['13456', 'ROBBERY', 'BODILY FORCE']
        c_2 = ['13456', 'ROBBERY', 'ARMED ROBBERY']
        c_3 = ['23145', 'THEFT', 'LOOTING']
        c_4 = ['98635', 'MURDER', 'STABBING']
        c_5 = ['54313', 'ROBBERY', 'BODILY FORCE']
        c_6 = ['63527', 'VANDALISM', 'GRAFFITI']
        c_7 = ['72514', 'ROBBERY', 'ARMED']
        crime_lines = [c_1, c_2, c_3, c_4, c_5, c_6, c_7]
        rob_1 = partner2.Crime('13456', 'ROBBERY')
        rob_2 = partner2.Crime('54313', 'ROBBERY')
        rob_3 = partner2.Crime('72514', 'ROBBERY')
        lst_of_crime = [rob_1, rob_2, rob_3]
        test_val = partner2.create_crimes(crime_lines)
        expected_val = lst_of_crime
        self.assertEqual(test_val, expected_val)

    def test_sort_crimes(self):
        # c_1 = crimetime.Crime('1', 'ROBBERY')
        # c_2 = crimetime.Crime('2', 'ROBBERY')
        # c_3 = crimetime.Crime('3', 'ROBBERY')
        # c_4 = crimetime.Crime('4', 'ROBBERY')
        # c_5 = crimetime.Crime('5', 'ROBBERY')
        # c_6 = crimetime.Crime('6', 'ROBBERY')
        # c_7 = crimetime.Crime('7', 'ROBBERY')
        # c_8 = crimetime.Crime('8', 'ROBBERY')
        # c_9 = crimetime.Crime('9', 'ROBBERY')
        # c_10 = crimetime.Crime('10', 'ROBBERY')
        # unsorted = [c_4, c_3, c_5, c_1, c_2]
        # unsorted_2 = [c_7, c_9, c_6, c_10, c_8]
        # test_case1 = crimetime.sort_crimes(unsorted)
        # test_case2 = crimetime.sort_crimes(unsorted_2)
        # expected1 = [crimetime.Crime('1', 'ROBBERY'), crimetime.Crime('2', 'ROBBERY'), crimetime.Crime('3', 'ROBBERY'),
        #              crimetime.Crime('4', 'ROBBERY'), crimetime.Crime('5', 'ROBBERY')]
        # expected2 = [crimetime.Crime('6', 'ROBBERY'), crimetime.Crime('7', 'ROBBERY'), crimetime.Crime('8', 'ROBBERY'),
        #              crimetime.Crime('9', 'ROBBERY'), crimetime.Crime('10', 'ROBBERY')]
        # self.assertEqual(test_case1, expected1)
        # self.assertEqual(test_case2, expected2)
        c_1 = partner1.Crime('1', 'ROBBERY')
        c_2 = partner1.Crime('2', 'ROBBERY')
        c_3 = partner1.Crime('3', 'ROBBERY')
        c_4 = partner1.Crime('4', 'ROBBERY')
        c_5 = partner1.Crime('5', 'ROBBERY')
        c_6 = partner1.Crime('6', 'ROBBERY')
        c_7 = partner1.Crime('7', 'ROBBERY')
        c_8 = partner1.Crime('8', 'ROBBERY')
        c_9 = partner1.Crime('9', 'ROBBERY')
        c_10 = partner1.Crime('10', 'ROBBERY')
        unsorted = [c_4, c_3, c_5, c_1, c_2]
        unsorted_2 = [c_7, c_9, c_6, c_10, c_8]
        test_case1 = partner1.sort_crimes(unsorted)
        test_case2 = partner1.sort_crimes(unsorted_2)
        expected1 = [partner1.Crime('1', 'ROBBERY'), partner1.Crime('2', 'ROBBERY'), partner1.Crime('3', 'ROBBERY'),
                     partner1.Crime('4', 'ROBBERY'), partner1.Crime('5', 'ROBBERY')]
        expected2 = [partner1.Crime('6', 'ROBBERY'), partner1.Crime('7', 'ROBBERY'), partner1.Crime('8', 'ROBBERY'),
                     partner1.Crime('9', 'ROBBERY'), partner1.Crime('10', 'ROBBERY')]
        self.assertEqual(test_case1, expected1)
        self.assertEqual(test_case2, expected2)

    def test_set_crimetime(self):
        c1 = partner1.Crime('1234', 'ROBBERY')
        partner1.set_crimetime(c1, 'Wednesday', 7, 17)
        c2 = partner1.Crime('1745', 'ROBBERY')
        c3 = partner1.Crime('4725', 'ROBBERY')
        c4 = partner1.Crime('1234', 'ROBBERY')
        c4.day_of_week = 'Wednesday'
        c4.month = 'July'
        c4.hour = '5PM'
        c5 = partner1.Crime('1745', 'ROBBERY')
        c6 = partner1.Crime('4725', 'ROBBERY')
        self.assertEqual(c1, c4)
        self.assertEqual(c2, c5)
        self.assertEqual(c3, c6)

    def test_update_crimes(self):
        crimes = [partner1.Crime('1', 'ROBBERY'), partner1.Crime('2', 'ROBBERY'), partner1.Crime('3', 'ROBBERY')]
        times = [['1', 'Tuesday', '01/23/16', '23:21'], ['2', 'Friday', '06/15/01', '13:26'],
                 ['3', 'Wednesday', '12/25/16', '23:56']]
        updated = partner1.update_crimes(crimes, times)
        c1 = partner1.Crime('1', 'ROBBERY')
        c2 = partner1.Crime('2', 'ROBBERY')
        c3 = partner1.Crime('3', 'ROBBERY')
        c1.day_of_week = 'Tuesday'
        c1.month = 'January'
        c1.hour = '11PM'
        c2.day_of_week = 'Friday'
        c2.month = 'June'
        c2.hour = '1PM'
        c3.day_of_week = 'Wednesday'
        c3.month = 'December'
        c3.hour = '11PM'
        expected = [c1, c2, c3]
        self.assertEqual(updated, expected)

    def test_find_crime(self):
        crimes = [partner1.Crime('1', 'ROBBERY'), partner1.Crime('2', 'ROBBERY'), partner1.Crime('3', 'ROBBERY')]
        self.assertEqual(partner1.find_crime(crimes, '1'), partner1.Crime('1', 'ROBBERY'))
        self.assertEqual(partner1.find_crime(crimes, '2'), partner1.Crime('2', 'ROBBERY'))
        self.assertEqual(partner1.find_crime(crimes, '3'), partner1.Crime('3', 'ROBBERY'))




















if __name__ == '__main__':
    unittest.main()
