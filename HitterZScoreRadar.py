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

STEPS TO RUN
1. Get the stats from a csv from this link:
    https://baseballsavant.mlb.com/leaderboard/custom?year=2021&type=batter&filter=&sort=3&sortDir=desc&min=q&selections=b
    _total_pa,on_base_plus_slg,wobacon,xwobacon,exit_velocity_avg,barrel_batted_rate,hard_hit_percent,
    &chart=false&x=b_total_pa&y=b_total_pa&r=no&chartType=beeswarm
    
    Make sure Qualified hitters is selected and press 'Download CSV'

2. Once the file is downlaoded, put it in the same directory as this code
3. Change the file name variable on line 40 (rigth after import modules) to match the name of your csv. Make sure to include .csv extension
4. Change the name of the player on line 42 (also right after import modules)
5. Run the code!
"""

#Import modules
import sys
import pandas as pd
import matplotlib.pyplot as plt
from math import pi


#Enter the name of the file you downloaded from Baseball Savant
fileName = 'radarstats2.csv'
#Change this to get the player's data that we want to chart
playerToChart = 'Aaron Judge'

#Read CSV file
data = pd.read_csv (r'C:/Users/ztand/Desktop/Python/'+fileName)
data['name'] = data[' first_name'] + ' ' + data['last_name']

#Get the means of each column
wobaconmean = data['wobacon'].mean()
evamean = data['exit_velocity_avg'].mean()
bbrmean = data['barrel_batted_rate'].mean()
xwobaconmean = data['xwobacon'].mean()
opsmean = data['on_base_plus_slg'].mean()
hhpmean = data['hard_hit_percent'].mean()

#Get the standard deviation of each column
wobaconsd = data['wobacon'].std()
evasd = data['exit_velocity_avg'].std()
bbrsd = data['barrel_batted_rate'].std()
xwobaconsd = data['xwobacon'].std()
opssd = data['on_base_plus_slg'].std()
hhpsd = data['hard_hit_percent'].std()

#Create z-score columns for each player and each stat
#Z-Score = (observed value - mean of the sample) / standard deviation of the sample
data['wobacon_zscore'] = (data['wobacon'] - wobaconmean) /wobaconsd
data['eva_zscore'] = (data['exit_velocity_avg'] - evamean)/evasd
data['bbr_zscore'] = (data['barrel_batted_rate']- bbrmean)/bbrsd
data['xwobacon_zscore'] = (data['xwobacon'] - xwobaconmean) /xwobaconsd
data['ops_zscore'] = (data['on_base_plus_slg'] - opsmean) /opssd
data['hhp_zscore'] = (data['hard_hit_percent'] - hhpmean) /hhpsd



#Get the Z-Scores and other stats from the DataFrame
player = data[data['name'].str.contains(playerToChart)]
ops = float(player['ops_zscore'])
wobacon = float(player['wobacon_zscore'])
xwobacon = float(player['xwobacon_zscore'])
eva = float(player['eva_zscore'])
bbr = float(player['bbr_zscore'])
hhp = float(player['hhp_zscore'])
year = str(player['year'])
pa = str(player['b_total_pa'])

stats = ['OPS', 'wOBACON', 'xwOBACON', 'AVG. EV', 'BARREL %','HARD HIT %']
values = [ops,wobacon,xwobacon,eva,bbr,hhp]

#Style and plot the Polar Chart
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
yearList = year.split(' ')
yearList2 = yearList[4].split('\n')
year = yearList2[0]
paList = pa.split(' ')
paList2 = paList[4].split('\n')
pa = paList2[0]
plt.title(playerToChart + '\n' + year + '\n' + pa + ' Plate Appearences')
plt.show()
