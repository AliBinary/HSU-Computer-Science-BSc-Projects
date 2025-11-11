from datetime import datetime

">>>   enter the data like this: 2022/2/20   <<<"
# dates in string format
dates = ["3/29",
         "4/11",
         "4/14",
         "4/19",
         "4/21",
         "4/28",
         "5/1",
         "5/9",
         "5/16",
         "5/20",
         "5/24",
         "5/29",
         "6/1",
         "6/4",
         "6/7",
         "6/17",
         "6/24",
         "7/3",
         "7/7",
         "7/15",
         "7/17"
         ]


def diff(str_d1, str_d2):
    # convert string to date object
    d1 = datetime.strptime(str_d1, "%m/%d")
    d2 = datetime.strptime(str_d2, "%m/%d")

    # difference between dates in timedelta
    delta = d2 - d1
    return delta.days


diffs = []
for i in range(len(dates) - 1):
    diffs.append(diff(dates[i], dates[i+1]))


print(diffs)
