#Some basic matplotlib.pyplot functions and features. Give them a try.
#Datasets available in SupervisedML repository.

"""from matplotlib import pyplot as plt
import numpy as np

# print(plt.style.available)

plt.style.use('fivethirtyeight')

x = [12,24,36,48,60,72,84,96]

indexx = np.arange(0,len(x))
width = 0.35


y = [12000,12312,31233,13564,12312,31290,39012,12232]

devy = [10000,20000,35000,31200,17000,54000,23000,26000]

# plt.plot(x,y, 'k--', label = 'What')
# plt.plot(x,y, color = 'k', linestyle = '--', marker = '.', label = 'What')
#
# plt.plot(x,devy, linewidth = '5', label = 'How')

plt.bar(indexx - width/2 ,devy, width = width ,label = 'What')
plt.bar(indexx + width/2 ,y, width = width, label = 'What')
plt.xticks(ticks=indexx, labels=x)

#Check format string color line marker on google fmt


plt.legend(['Python','JS'])
plt.xlabel("Age")
plt.ylabel("Money")
plt.title("Learning (money)")
plt.tight_layout()
# plt.legend(['First','Second'])

plt.show()
"""


"""
from matplotlib import pyplot as plt
import numpy as np
import csv
import pandas as pd

# print(plt.style.available)

plt.style.use('fivethirtyeight')

with open('ex.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)
    print(row)
    # print(row['Rope'].split(';'))

    x = np.random.random(50) * 100
    y = np.random.random(50) * 100

    # plt.scatter(x,y)

    plt.scatter(x, y, c='#00f', s=150, marker='.', alpha=0.3)  # colour, size, marker, transperency
    plt.show()
"""


"""
import numpy as np
from matplotlib import pyplot as plt

x = np.random.random(50) * 100
y = np.random.random(50) * 100

# plt.scatter(x,y)

plt.scatter(x,y,c='#00f',s=150,marker='*',alpha=0.3) #colour, size, marker, transperency
#Color maps are also available getting different colored dots everywhere.
plt.show()
"""


"""
import numpy as np
from matplotlib import pyplot as plt

ages = np.random.normal(20,1.5,1000)

plt.hist(ages,bins=20,cumulative=True) #arg,sections,order
# plt.hist(ages,bins=[ages.min(),16,17,18,20,ages.max()])

plt.show()
"""
"""
import numpy as np
from matplotlib import pyplot as plt

lang = ['.py', '.cpp', '.c', 'asm', 'go']
nums = [59, 21, 34, 12, 43]
explode =[0.2,0.1,0,0,0.0025] #highliting by taking it out of the chart

plt.pie(nums,labels=lang,explode=explode,autopct="%.2f%%",pctdistance=1.4,startangle=90)
plt.show()
"""
"""
Stack Plots are similar. Continuous filled graphs under lines. similar syntax.
Filling area between lines and axis is also similar using fill_between function.
We can also provide conditions in the function using where= feature and alpha for blur.
As well as a 3rd value (int) where line gets upside down as well.
Use 3rd value as list to form graph between lines.

Box plots are also there but they are not usually used.

Must see different attributes for different functions for the best input.

Scatterplots have mulitple attributes like sizes, colours, edgecolor, linewidth and cmap.

See Corey Schafer fill between code for reference.

"""
"""
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('fivethirtyeight')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot_date(dates,y,linestyle='solid',linewidth=1)

plt.gcf().autofmt_xdate() #Get Current figure. An autoformat method.

date_format = mpl_dates.DateFormatter('%b, %d %Y')

plt.gca().xaxis.set_major_formatter(date_format)

# data = pd.read_csv('BigData.csv')

# data['Date'] = pd.to_datetime(data['Date'])
# data.sort_values('Date', inplace=True)

# price_date = data['Date']
# price_close = data['Close']

# plt.title('Bitcoin Prices')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()
"""
"""
#SEE LIVE DATA PLOTTING IN MATPLOTLIB BECAUSE IT IS CONFUSING


import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

plt.plot(x_vals, y_vals)


index = count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))


plt.tight_layout()
plt.show()


# data = pd.read_csv('BigData.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']
"""
"""
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

ax1.plot(ages, py_salaries, color='Red', linestyle='-', linewidth= 1, label='Python')
ax1.plot(ages, js_salaries, color='Blue', linestyle='-', linewidth= 1, label='JavaScript')

ax2.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax1.legend()
ax1.set_title('Python/JavaScript')
# ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')

ax2.legend()
ax2.set_title('All developers')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

#Can create different figures as well

fig.savefig('Subplots.png')
#Use savefig to save the image of the figure
"""
