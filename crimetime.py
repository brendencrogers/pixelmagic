"""Crime time Project 3
CPE 101
Spring 2020
Author: Brenden Rogers
"""

import sys
import copy


def main(argv):
    """Write to crime file"""
    crime_lines = []
    with open(argv[1], 'r') as crime_file:  # crimes.tsv
        for a in crime_file:
            a = str(a)
            lines = a.split('\t')
            crime_lines.append(lines)
    crimes = create_crimes(crime_lines)
    crimes_sort = sort_crimes(crimes)
    times = []
    with open(argv[2], 'r') as time_file:  # times.tsv
        for n in time_file:
            n = str(n)
            time_lines = n.split('\t')
            times.append(time_lines)
    times.remove(times[0])
    up_crimes = update_crimes(crimes_sort, times)
    day_most = get_day_most(up_crimes)
    month_most = get_month_most(up_crimes)
    hour_most = get_most_hour(up_crimes)
    rob_sums = get_rob_nums(up_crimes)
    up_crimes = ''.join([str(x) for x in up_crimes])
    with open('robberies.tsv', 'w') as robberies:
        robberies.write('ID' + '\t' + 'Category' '\t' + 'DayOfWeek' +
                        '\t' + 'Month' + '\t' + 'Hour' + '\n' + up_crimes)
    print('NUMBER OF PROCESSED ROBBERIES: ' + str(rob_sums))
    print('DAY WITH MOST ROBBERIES: ' + day_most)
    print('MONTH WITH MOST ROBBERIES: ' + month_most)
    print('HOUR WITH MOST ROBBERIES: ' + hour_most)


class Crime:
    """Contains crime data with each object

    Attributes:
        crime_id (str): Crime ID number
        category (str): Crime category
        day_of_week (str): day of week crime took place
        month (str): month crime took place
        hour (int): hour crime took place (AM/PM)
    """
    def __init__(self, crime_id, category):
        """To initialize 2 objects

        Args:
            crime_id: Crime ID number
            category: Crime category
        """
        self.crime_id = crime_id
        self.category = category
        self.day_of_week = None
        self.month = None
        self.hour = None

    def __eq__(self, other):
        return isinstance(other, Crime) and self.crime_id == other.crime_id

    def __repr__(self):
        return "{}\t{}\t{}\t{}\t{}\n".format(self.crime_id, self.category, self.day_of_week, self.month, self.hour)


def create_crimes(lines) -> list:
    """Generate list of unique crime objects (Robberies)

    Args:
        lines (list): list of strings, each a line from crimes file

    Returns:
        list: list of crime objects, for each UNIQUE robbery
    """
    crimes = []
    for line in lines:
        if line[1] != 'ROBBERY':
            continue
        _id = line[0]
        dup = False
        for crime in crimes:
            if _id == crime.crime_id:
                dup = True
                break
        if dup is False:
            crimes.append(Crime(_id, line[1]))
    return crimes


def sort_crimes(crimes) -> list:
    """Sort crimes by ID number (insertion)

    Args:
        crimes (list): list of crime objects

    Returns:
        list: crimes sorted
    """
    sorted_lst = copy.copy(crimes)
    size = len(sorted_lst)
    for i in range(1, size):
        j = i
        while j > 0 and int(sorted_lst[j-1].crime_id) > int(sorted_lst[j].crime_id):
            sorted_lst[j-1].crime_id, sorted_lst[j].crime_id = sorted_lst[j].crime_id, sorted_lst[j-1].crime_id
            j -= 1
    return sorted_lst


def set_crimetime(crime, day_of_week, month, hour):
    """Update time data attributes that have been initialized to None

    Args:
        crime (Crime): crime object
        day_of_week (str): day of week
        month (int): month number
        hour (int): hour number (0-23)

    Returns:
        Crime: updated Crime objects
    """
    crime.day_of_week = day_of_week
    months = ['January', 'February', "March", 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    month = month - 1
    crime.month = months[month]
    am_hours = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM']
    pm_hours = ['12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM']
    if hour < 12:
        crime.hour = am_hours[hour]
    else:
        hour = hour - 12
        crime.hour = pm_hours[hour]


def update_crimes(crimes, lines):
    """Updates attributes of crime objects

    Args:
        crimes (list): Sorted crime objects
        lines (list): list of lines from times.tsv

    Returns:
        list: updated list of crime objects
    """
    count = 0
    for i in lines:
        time = i[3]
        hour = time[0:2]
        day_of_week = i[1]
        date = i[2]
        month = (date[0:2])
        match = find_crime(crimes, i[0])
        if match is not None:
            set_crimetime(match, day_of_week, int(month), int(hour))
            count += 1
    unique = []
    for a in crimes:
        if a not in unique:
            unique.append(a)
    return unique


def find_crime(crimes, crime_id) -> Crime:
    """To use binary search to find crime object

    Args:
        crimes (list): List of sorted crime objects
        crime_id (str): string of crime ID number

    Returns:
        Crime: crime object with correlating ID
    """
    base = 0
    size = len(crimes) - 1
    while size >= base:
        crime_id = int(crime_id)
        mid = (base + size) // 2
        current = crimes[mid]
        if int(current.crime_id) == crime_id:
            return current
        if crime_id < int(current.crime_id):
            size = mid - 1
        else:
            base = mid + 1


def get_rob_nums(crimes):
    """Get sum of robberies processed

    Args:
        crimes (list): list of sorted crime objects

    Returns:
        int: number of robberies processed
    """
    return len(crimes)


def get_day_most(crimes):
    """Searches for day of week with most robberies

    Args:
        crimes (list): list of crime objects

    Returns:
        str: Day of week with most robberies
    """
    mon = 0
    tue = 0
    wed = 0
    thu = 0
    fri = 0
    sat = 0
    sun = 0
    for i in crimes:
        if i.day_of_week == 'Monday':
            mon += 1
        elif i.day_of_week == 'Tuesday':
            tue += 1
        elif i.day_of_week == 'Wednesday':
            wed += 1
        elif i.day_of_week == 'Thursday':
            thu += 1
        elif i.day_of_week == 'Friday':
            fri += 1
        elif i.day_of_week == 'Saturday':
            sat += 1
        else:
            sun += 1
    days = {mon: 'Monday', tue: 'Tuesday',
            wed: 'Wednesday', thu: 'Thursday', fri: 'Friday', sat: 'Saturday',
            sun: 'Sunday'}
    day = max(days)
    day = days.get(day)
    return day


def get_month_most(crimes):
    """Returns month with most robberies

    Args:
        crimes (list): list of time updated crime objects

    Returns:
        str: Month with most
    """
    jan = 0
    feb = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    aug = 0
    sep = 0
    oct = 0
    nov = 0
    dec = 0
    for i in crimes:
        if i.month == 'January':
            jan += 1
        elif i.month == 'February':
            feb += 1
        elif i.month == 'March':
            mar += 1
        elif i.month == 'April':
            apr += 1
        elif i.month == 'May':
            may += 1
        elif i.month == 'June':
            jun += 1
        elif i.month == 'July':
            jul += 1
        elif i.month == 'August':
            aug += 1
        elif i.month == 'September':
            sep += 1
        elif i.month == 'October':
            oct += 1
        elif i.month == 'November':
            nov += 1
        else:
            dec += 1
    months = {jan: 'January', feb: 'February', mar: 'March', apr: 'April'
              , may: 'May', jun: 'June', jul: 'July', aug: 'August',
              sep: 'September', oct: 'October', nov: 'November',
              dec: 'December'}
    max_month = max(months)
    month = months.get(max_month)
    return month


def get_most_hour(crimes):
    """To get the hour with the most crimes

    Args:
        crimes (list): list of crime objects

    Returns:
        str: Hour with most robberies
    """
    hours = []
    for i in crimes:
        hours.append(i.hour)
    twelve_am = hours.count('12AM')
    one_am = hours.count('1AM')
    two_am = hours.count('2AM')
    three_am = hours.count('3AM')
    four_am = hours.count('4AM')
    five_am = hours.count('5AM')
    six_am = hours.count('6AM')
    sev_am = hours.count('7AM')
    eight_am = hours.count('8AM')
    nine_am = hours.count('9AM')
    ten_am = hours.count('10AM')
    elev_am = hours.count('11AM')
    twelve_pm = hours.count('12PM')
    one_pm = hours.count('1PM')
    two_pm = hours.count('2PM')
    three_pm = hours.count('3PM')
    four_pm = hours.count('4PM')
    five_pm = hours.count('5PM')
    six_pm = hours.count('6PM')
    sev_pm = hours.count('7PM')
    eight_pm = hours.count('8PM')
    nine_pm = hours.count('9PM')
    ten_pm = hours.count('10PM')
    elev_pm = hours.count('11PM')
    hour_dic = {twelve_am: '12AM', one_am: '1AM', two_am: '2AM', three_am: '3AM', four_am: '4AM',
                five_am: '5AM', six_am: '6AM', sev_am: '7AM', eight_am: '8AM',
                nine_am: '9AM', ten_am: '10AM', elev_am: '11AM', twelve_pm: '12PM',
                one_pm: '1PM', two_pm: '2PM', three_pm: '3PM',
                four_pm: '4PM', five_pm: '5PM', six_pm: '6PM', sev_pm: '7PM', eight_pm: '8PM',
                nine_pm: '9PM', ten_pm: '10PM', elev_pm: '11PM'}
    max_hour = max(twelve_am, one_am, two_am, three_am, four_am, five_am, six_am, sev_am, eight_am, nine_am, ten_am,
                   elev_am, twelve_pm, one_pm, two_pm, three_pm, four_pm, five_pm, six_pm, sev_pm, eight_pm, nine_pm,
                   ten_pm, elev_pm)
    hour = hour_dic.get(max_hour)
    return hour


if __name__ == '__main__':
    main(sys.argv)
