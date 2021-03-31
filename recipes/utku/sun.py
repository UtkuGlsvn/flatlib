from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.tools.chartdynamics import ChartDynamics


# Build a chart for a date and location
date = Datetime('1997/01/20', '05:00', '+2:50')
pos = GeoPos('39:96', '32:81')
chart = Chart(date, pos)
sun = chart.getObject(const.SUN)
print("--------------- SUN")
print(sun.sign)#gunes burc
print(sun.gender())#gunes burc cinsiyet
# moon = chart.getObject(const.MOON)
# print("--------------- SUN")
# print(moon.sign)#ay burcu