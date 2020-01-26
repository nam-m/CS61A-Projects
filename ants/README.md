## Project 3: Ants Vs.SomeBees (ants)
A [tower defense](https://en.wikipedia.org/wiki/Tower_defense) game called Ants Vs. SomeBees. As the ant queen, you populate your colony with the bravest ants you can muster. Your ants must protect their queen from the evil bees that invade your territory. Irritate the bees enough by throwing leaves at them, and they will be vanquished. Fail to pester the airborne intruders adequately, and your queen will succumb to the bees' wrath. This game is inspired by PopCap Games' [Plants Vs. Zombies](https://en.wikipedia.org/wiki/Tower_defense)

![GUI pic](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/splash.png?raw=true)

### List of Ants

Class | Food Cost | Armor | Action
-|-|-|-
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/bee-resized.gif) <br> Bee |  | 1 | Deals 1 damage to Ant in its place
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_harvester.gif?raw=true) <br> Harvester Ant | 2 | 1 | Adds 1 food to colony
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_thrower.gif?raw=true) <br> Thrower Ant | 3 | 1 | Attacks nearest Bee ahead
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_shortthrower-resized.gif) <br> Short Thrower | 2 | 1 | Attacks Bee at most 3 places ahead
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_longthrower-resized.gif) <br> Long Thrower | 2 | 1 | Attacks Bee at least 5 places ahead
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_fire.gif?raw=true) <br> Fire Ant | 5 | 3 | Reflect Bee's damage <br> Damages all Bees in its place when killed
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_hungry.gif?raw=true) <br> Hungry Ant | 4 | 1 | Eats random Bee in its place and spends 3 turns digesting before eating again
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_ninja.gif?raw=true) <br> Ninja Ant | 5 | 1 | Damages all Bees that fly past it
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_wall.gif?raw=true) <br> Wall Ant | 4 | 4 | Does nothing
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_bodyguard-resized.gif) <br> Bodyguard Ant | 4 | 2 | Protects an Ant and takes damage instead while allowing protected ant to perform its action
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_tank-resized.gif) <br> Tank Ant | 6 | 2 | Same as Bodyguard Ant ant deals 1 damage to all Bees in its place
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_scuba.gif?raw=true) <br> ScubaThrower Ant | 6 | 1 | Same as Thrower Ant but can be placed on Water
![](https://github.com/nam-m/CS61A-Projects/blob/master/ants/assets/insects/ant_queen.gif?raw=true) <br> Queen Ant | 7 | 1 | Only 1 true Queen Ant <br> Doubles damage of all Ants behind her <br> Bees win if she is killed 


### To be updated...
