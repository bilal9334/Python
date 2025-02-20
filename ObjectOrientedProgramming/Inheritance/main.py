from enemy import Enemy, Troll, Vampyre, VampyreKing

# random_monster = Enemy("Basic Enemy", 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
#
# random_monster.take_damage(8)
# print(random_monster)
#
# random_monster.take_damage(9)
# print(random_monster)

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
# another_troll.take_damage(18)
# print(another_troll)
#
# brother = Troll("Urg")
# print(brother)
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# print()
#
# vamp1 = Vampyre("Dracula")
# print(vamp1)
# vamp1.take_damage(5)
# print(vamp1)
#
# print("-" * 40)
# another_troll.take_damage(30)
# print(another_troll)
#
# # while vamp1._alive:
# #     vamp1.take_damage(1)
# #         # print(vamp1)
#
# vamp1._lives = 0
# vamp1._hit_points = 1
# print(vamp1)

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)
