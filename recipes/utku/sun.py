from flatlib import const
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.tools.chartdynamics import ChartDynamics
from flatlib.protocols import almutem


# Build a chart for a date and location
date = Datetime('2020/01/20', '05:00', '+2:50')
pos = GeoPos('39:57', '32:53')
chart = Chart(date, pos)
sun = chart.getObject(const.SUN)
#print("--------------- SUN")
print("Güneş Burç :"+sun.sign)#gunes burc
moon = chart.getObject(const.MOON)
print("Ay Burç :"+moon.sign)#gunes burc
#print(sun.signlon)#gunes burc
#print(sun.gender())#gunes burc cinsiyet
#print(sun)
print("------------------EVLER-----------")
#Ev listesi
homeList = [const.HOUSE1,const.HOUSE2,const.HOUSE3,const.HOUSE4,const.HOUSE5,const.HOUSE6,const.HOUSE7,const.HOUSE8,const.HOUSE9,const.HOUSE10,const.HOUSE11,const.HOUSE12]
house1 = chart.get(const.HOUSE12)
for i in homeList:
    print("{0}:   {1} ".format(i,chart.get(i).sign))


alm = almutem.compute(chart)

# # Sun relation
# relation = accidental.sunRelation(obj, sun)
# print(relation)

# print("--------------ASPECT-------------")
# aspect = aspects.getAspect(sun, moon, const.ALL_ASPECTS)
# print(aspect.inOrb)
# moon = chart.getObject(const.MOON)
# print("--------------- SUN")
# print(moon.sign)#ay burcu