import twint
from datetime import datetime as dt, timedelta as td

c = twint.Config()
c.Search = "#covid19dk"
c.Min_replies = 1

pressemoeder = [
    ("2020-03-11 20:30:00", "2020-03-11 23:59:59"),
    ("2020-03-13 19:00:00", "2020-03-13 23:59:59"),
    ("2020-03-15 12:00:00", "2020-03-15 23:59:59"),
    ("2020-03-17 19:00:00", "2020-03-17 23:59:59"),
    ("2020-03-23 15:00:00", "2020-03-23 23:59:59"),
    ("2020-03-30 17:30:00", "2020-03-30 23:59:59"),
    ("2020-04-06 20:00:00", "2020-04-06 23:59:59"),
    ("2020-04-14 16:00:00", "2020-04-14 23:59:59"),
]

for start, end in pressemoeder: 
    print(start)
    c.Since = start
    c.Until = end
    c.Store_csv = True
    c.Output = f"Corona-Tweets-{start}"
    twint.run.Search(c)