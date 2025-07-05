import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]


# Vizualization Begins Here...

# 1.Bar chart

plt.bar(range(len(games)), viewers, color='orange')
# Adding X and Y axis labels
plt.xlabel('Games')
plt.ylabel('Viewers')

# Setting up ticks & Adding tick labels

ax = plt.subplot()

ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ax.set_xticklabels(games, rotation=30)

# Adding Legends
plt.legend(["Twitch"])

# Adding title for the bar chart
plt.title('Featured Games Viewers')

plt.show()

# We can add plt.clf() to clear the current figure, our bar graph, before creating our next figure, the pie chart

plt.clf()

# 2.Pie Chart

# Creating an array of colors for different countries

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

# Making more visual

#Slicing out US from pie chart
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)

# Setting up axis
plt.axis('equal')

# Adding Title for the pie chart
plt.title("League of Legends Viewers' Whereabouts")

# Adding Legends
plt.legend(labels, loc="right")

plt.show()

# We can add plt.clf() to clear the current figure, our pie chart,before creating our next figure, the line graph

plt.clf()

# 3.Line Graph

plt.plot(hour, viewers_hour)

# For some uncertainity in Viewers hour, upper and lower bound for errors are added

y_upper = [i + (i * 0.15) for i in viewers_hour]
y_lower = [i - (i * 0.15) for i in viewers_hour]

plt.fill_between(hour, y_upper, y_lower, alpha=0.2)

# Adding X and Y axis labels
plt.xlabel('Hours')
plt.ylabel('Viewers')

# Setting up ticks & Adding tick labels

ax = plt.subplot()

ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])

# Adding Legends
plt.legend(['2015-01-01'])

# Adding title for the bar chart
plt.title('Viewers View By Hours Basis')

plt.show()
