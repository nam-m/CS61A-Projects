from ants import *
import ants, importlib
importlib.reload(ants)

# beehive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (2, 9)
# colony = AntColony(None, beehive, ant_types(), layout, dimensions)

# thrower = ThrowerAnt()
# ant_place = colony.places["tunnel_0_0"]
# ant_place.add_insect(thrower)

# near_bee = Bee(2) # A Bee with 2 armor
# far_bee = Bee(3)  # A Bee with 3 armor
# near_place = colony.places['tunnel_0_3']
# far_place = colony.places['tunnel_0_6']
# near_place.add_insect(near_bee)
# far_place.add_insect(far_bee)
# nearest_bee = thrower.nearest_bee(colony.beehive)

# place = colony.places['tunnel_0_4']
# fire = FireAnt(armor=1)
# place.add_insect(fire)        # Add a FireAnt with 1 armor
# place.add_insect(Bee(3))      # Add a Bee with 3 armor
# place.add_insect(Bee(5))      # Add a Bee with 5 armor
# print(place.bees)
# print(type(place.bees))

# # Testing HungryAnt eats and digests
# hungry = HungryAnt()
# bee1 = Bee(1000)              # A Bee with 1000 armor
# place = colony.places["tunnel_0_0"]
# place.add_insect(hungry)
# place.add_insect(bee1)         # Add the Bee to the same place as HungryAnt
# hungry.action(colony)
# print(bee1.armor)
# bee2 = Bee(1)                 # A Bee with 1 armor
# place.add_insect(bee2)
# for _ in range(3):
#     hungry.action(colony)     # Digesting...not eating
# print(bee2.armor)
# hungry.action(colony)
# print(bee2.armor)

# # Testing bodyguard performs thrower's action
# bodyguard = BodyguardAnt()
# thrower = ThrowerAnt()
# bee = Bee(2)
# # Place thrower before bodyguard
# colony.places["tunnel_0_0"].add_insect(thrower)
# colony.places["tunnel_0_0"].add_insect(bodyguard)
# colony.places["tunnel_0_3"].add_insect(bee)
# bodyguard.action(colony)
# bee.armor

beehive = ants.Hive(ants.AssaultPlan())
dimensions = (2, 9)
colony = ants.AntColony(None, beehive, ants.ant_types(), ants.dry_layout, dimensions)
ants.bees_win = lambda: None
queen = ants.QueenAnt()
impostor = ants.QueenAnt()
front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
tunnel = [colony.places['tunnel_0_{0}'.format(i)] for i in range(9)]
tunnel[1].add_insect(back_ant)
tunnel[7].add_insect(front_ant)
tunnel[4].add_insect(impostor)
impostor.action(colony)
print(impostor.armor)          # Impostors must die!
print(tunnel[4].ant is None)

tunnel[4].add_insect(queen)
print(queen.action(colony))