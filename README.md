# MLBHitterZScore
A Python program that shows how a hitter compares to the mean of a sample of MLB hitters in certain statistics using a Polar Chart

## About
This is a program that will show an MLB hitters Z-Score for the following statistics:
- [wOBA](https://www.mlb.com/glossary/advanced-stats/weighted-on-base-average)
- [xwOBA](https://www.mlb.com/glossary/statcast/expected-woba)
- [OPS](https://www.mlb.com/glossary/standard-stats/on-base-plus-slugging)
- [Hard Hit %](https://www.mlb.com/glossary/statcast/hard-hit-rate)
- [Barrel %](https://www.mlb.com/glossary/statcast/hard-hit-rate)
- [Average Exit Velo](https://www.mlb.com/glossary/statcast/exit-velocity)

The reason I sued these statistics is because I believe these are extremly useful for evaluating a hitter. I will like a glossary to each so you can read more about what each statistic actually means and why it is useful for player evaluation.

For each one of these statistics, I computed the mean and standard deviation of the sample that is being worked with (Qualified MLB Hitters, meaning they have a certain amount of plate appearences depending on how many games have been played). I then calculate the Z-Score so we can see how they compare to the mean. The Z-Scores are then plotted in a Radar Chart (also called Polar Chart) so we can visualize our Z-Scores. The general rule of thumb is that if the shaded area is larger, the player is better.

## How to Run
Note - It is reccomended to use the [Spyder IDE](https://www.spyder-ide.org/) to run this as it is great for Data Vis and Python
As of the initial commit, to run the program, the step are:
1. Go to [this link](https://baseballsavant.mlb.com/leaderboard/custom?year=2021&type=batter&filter=&sort=5&sortDir=asc&min=q&selections=b_total_pa,on_base_plus_slg,woba,xwoba,exit_velocity_avg,barrel_batted_rate,hard_hit_percent,&chart=false&x=b_total_pa&y=b_total_pa&r=no&chartType=beeswarm)
2. Make sure you have the following columns (OPS, wOBA, xwOBA, Avg EV (MPH), Barrel%, Hard Hit %) and make sure Minimum PA is set to 'Q' for all qualified hitters
3. Click the 'Update' button
4. Download the csv and put it in the same directory as this program (NOTE - There is a CSV in this repo named <em>radarstats4.csv</em> that is an example of one. Refer to that to see what it should look like. You can also use that as a test file)
5. Change the file name varaible on line 40 to the name of your file 
6. Change the name of the player you want to visualize on line 42
7. Run and see the plot!


## Extra
Something to be aware of is that these Z-Score numbers don't mean a ton until about the All-Star break. The reason being we need a longer sample period to get an idea of what the league averages look like for ever stat, and also it's always a good idea to use a larger sample when evaluating a single player. That all being said, this program is still fun to use and it is neat to see how players stack up against eachother in terms of these vvisualizations.

## Examples
I am going to run two samples, one of a player with great stats and one of a player with bad stats.
### Sample 1 - Mike Trout
![image](https://user-images.githubusercontent.com/68918006/114806094-2951ee80-9d72-11eb-88d6-75a7965fe703.png)
### Sample 2 - Nick Madrigal
![image](https://user-images.githubusercontent.com/68918006/114806148-3ec71880-9d72-11eb-8256-90dba39228ba.png)

If we take a look at the first of two samples, we can see that Mike Trout is off to an extremly hot start. He is at least over 2 standard deviations better than the mean in 5/6 stats that we are visualizing. This means that he is performing well above the league average in every statistic.
If we look at Madrigal though, we see that he iis off to a very slow start. He is in the bottom 1% of the league in terms of his Hard Hit%, and his other stats are not much better.
As you can see from these samples, Mike Trout's shaded area is far bigger than Nick Madrigals, and he is off to a better start, so the visuilization checks out.

## Version Updates
#### Current Version: 1.0.3
- Updated stats to be wOBA and xwOBA instead of wOBACON and xwOBACON. Gives a better idea of how a hitter is performing since it also includes walks, hbp, etc. (Other ways to reach base besides getting hits).
- Added logic to color the charts based on how well the player compares to others. If the sum of all of a players Z-Scores is greater than the mean of the sum of all Z-Scores, the chart will be blue. Otherwise, the chart will be red.
