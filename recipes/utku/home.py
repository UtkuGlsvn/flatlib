from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.tools.chartdynamics import ChartDynamics


# Build a chart for a date and location
date = Datetime('1997/01/20', '01:00', '+3:50')
pos = GeoPos('38:55', '27:50')
chart = Chart(date, pos)
sun = chart.getObject(const.SUN)
print("--------------- SUN")
print(sun.sign)#günes yükselen