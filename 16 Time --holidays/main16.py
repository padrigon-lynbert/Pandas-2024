import pandas as pd

df = pd.read_csv('16 Time --holidays/appl.csv')

pd.date_range(start='7-1-2017', end='7-30-2017', freq='D')

from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng = pd.date_range(start='7-1-2017', end='7-21-2017', freq=usb)

df.set_index(rng, inplace=True)


from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday

class myBirthDayCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birth Day', month=6, day=20, observance=nearest_workday)
    ]
myc = CustomBusinessDay(calendar=myBirthDayCalendar())

print(pd.date_range(start='6/1/2017', end='6/30/2017', freq=myc))