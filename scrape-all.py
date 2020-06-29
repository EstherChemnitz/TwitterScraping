import twint
from datetime import datetime as dt, timedelta as td
from dateutil import parser
import time

c = twint.Config()
c.Search = ""
c.Lang = "da"
dwell = 10*60 # Ten Minutes
interval = td(hours=1)

pressemoeder = [
    #("2020-03-11 20:30:00", "2020-03-11 23:59:59"),
    #("2020-03-13 19:00:00", "2020-03-13 23:59:59"),
    ("2020-03-13 19:00:00", "2020-03-13 19:26:02"),
    ("2020-03-15 12:00:00", "2020-03-15 23:59:59"),
    ("2020-03-17 19:00:00", "2020-03-17 23:59:59"),
    ("2020-03-23 15:00:00", "2020-03-23 23:59:59"),
    ("2020-03-30 17:30:00", "2020-03-30 23:59:59"),
    ("2020-04-06 20:00:00", "2020-04-06 23:59:59"),
    ("2020-04-14 16:00:00", "2020-04-14 23:59:59"),
]

def fs(s): return s.strftime("%Y-%m-%d %H:%M:%S")

for start, end in pressemoeder: 
    sd = parser.parse(start)
    ed = parser.parse(end)
    step = parser.parse(end)
    while step > sd:
        c.Until = fs(step)
        step -= interval
        c.Since = fs(step)
        print((f"Fetching danish tweets from {c.Since} to {c.Until}..."))
        c.Store_csv = True
        c.Output = f"all-tweets/All-Tweets-{c.Since}-{c.Until}"
        twint.run.Search(c)
        now = time.time()
        while time.time() < now+dwell:
            time_left = now+dwell - time.time()
            print(f"   {round(time_left/60,2)} minutes left before next run       ", end="\r", flush=True)
            time.sleep(3)
