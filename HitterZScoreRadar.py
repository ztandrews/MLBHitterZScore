# -*- coding: utf-8 -*-
"""
@auth: ztandrews

Create a Radar chart that plots an MLLB hitters Z-Scores for certain statistics.
The visualization will give us a good idea of how the hitter comaprees to the average MLB hitter.

The stats we will be using are:
    - wobacon
    - xwobacon
    - OPS
    - Hard Hit %
    - Barrel %
    - Avg Exit Velo
    - k%
    - BB%


MAKE ANOTHER WITH ACTUAL VS EXPECTED STATS
"""

#Import modules
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pi

data = pd.read_csv (r'C:/Users/ztand/Desktop/Python/radarstats2.csv')
data['name'] = data[' first_name'] + ' ' + data['last_name']

#Get the means of each column
kmean = data['b_k_percent'].mean()
bbmean = data['b_bb_percent'].mean()
wobaconmean = data['wobacon'].mean()
evamean = data['exit_velocity_avg'].mean()
bbrmean = data['barrel_batted_rate'].mean()
xwobaconmean = data['xwobacon'].mean()
opsmean = data['on_base_plus_slg'].mean()
hhpmean = data['hard_hit_percent'].mean()

#Get the standard deviation of each column
ksd = data['b_k_percent'].std()
bbsd = data['b_bb_percent'].std()
wobaconsd = data['wobacon'].std()
evasd = data['exit_velocity_avg'].std()
bbrsd = data['barrel_batted_rate'].std()
xwobaconsd = data['xwobacon'].std()
opssd = data['on_base_plus_slg'].std()
hhpsd = data['hard_hit_percent'].std()

#Create z-score columns for each player and each stat
#Z-Score = (observed value - mean of the sample) / standard deviation of the sample
data['k_zscore'] = (data['b_k_percent'] - kmean)/ksd
data['bb_zscore'] = (data['b_bb_percent'] - bbmean)/bbsd
data['wobacon_zscore'] = (data['wobacon'] - wobaconmean) /wobaconsd
data['eva_zscore'] = (data['exit_velocity_avg'] - evamean)/evasd
data['bbr_zscore'] = (data['barrel_batted_rate']- bbrmean)/bbrsd
data['xwobacon_zscore'] = (data['xwobacon'] - xwobaconmean) /xwobaconsd
data['ops_zscore'] = (data['on_base_plus_slg'] - opsmean) /opssd
data['hhp_zscore'] = (data['hard_hit_percent'] - hhpmean) /hhpsd

#Change this to get the player's data that we want to chart
playerToChart = 'Mike Trout'

player = data[data['name'].str.contains(playerToChart)]
ops = float(player['ops_zscore'])
wobacon = float(player['wobacon_zscore'])
xwobacon = float(player['xwobacon_zscore'])
eva = float(player['eva_zscore'])
bbr = float(player['bbr_zscore'])
hhp = float(player['hhp_zscore'])
kp =  float(player['k_zscore'])
bbp = float(player['bb_zscore'])

year = str(player['year'])
pa = str(player['b_total_pa'])

stats = ['OPS', 'WOBACON', 'xWOBACON', 'AVG. EX VELO', 'BARREL RATE','HARD HIT %']
values = [ops,wobacon,xwobacon,eva,bbr,hhp]

fig = plt.figure(figsize=(25,25))
ax = plt.subplot(polar="True")

N= len(stats)
values+= values[:1]

angles = [n/float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

plt.polar(angles, values, marker='.')
plt.fill(angles,values,alpha=.3)
plt.xticks(angles[:-1], stats)
ax.set_rlabel_position(30)
plt.yticks([-3,-2,-1,0,1,2,3], color='grey',size=20)
plt.ylim(-3,3)


'''
fig = plt.figure(figsize=(25,25))
ax = plt.subplot(polar="True")
plt.polar(stats,values, marker='.')
plt.fill(stats,values,alpha=0.1)
ax.set_rlabel_position(25)
plt.xticks(stats)
plt.yticks([-3,-2,-1,0,1,2,3], color='grey',size=25)
'''

yearList = year.split(' ')
yearList2 = yearList[4].split('\n')
year = yearList2[0]

paList = pa.split(' ')
paList2 = paList[4].split('\n')
pa = paList2[0]


plt.title(playerToChart + '\n' + year + '\n' + pa + ' Plate Appearences')

plt.show()
