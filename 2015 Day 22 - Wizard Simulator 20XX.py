from collections import namedtuple
from itertools import permutations
from time import sleep

filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 22 Advent of Code Input.txt"
with open(filePath) as f:
    lines = f.readlines()
    bossHP = int(''.join([ch for ch in lines[0] if ch.isnumeric()]))
    bossDmg = int(''.join([ch for ch in lines[1] if ch.isnumeric()]))

playerHP = 50
playerMana = 500
playerArmor = 0

# GO TO THE POST OFFICE

Spell = namedtuple("Spell", ['name', 'cost', 'dmg', 'duration', 'HPup', 'armorUp', 'manaUp', 'active'])

magicMissile = Spell("Magic Missile", 53, 4, 1, 0, 0, 0, False)
drain = Spell("Drain", 73, 2, 1, 2, 0, 0, False)
shield = Spell("Shield", 113, 0, 6, 0, 7, 0, False)
poison = Spell("Poison", 173, 3, 6, 0, 0, 0, False)
recharge = Spell("Recharge", 229, 0, 5, 0, 0, 101, False)

spells = [magicMissile, drain, shield, poison, recharge]

virtualBossHP = bossHP
maxCastsNecessary, remain = divmod(virtualBossHP, drain.dmg)
virtualPlayerMana = playerMana
maxTurns = 0
while virtualBossHP > 0:
    print(f"Initial {virtualPlayerMana=}")
    castsBeforeNextRecharge = (virtualPlayerMana - recharge.cost) // drain.cost
    print(f"{castsBeforeNextRecharge=}")
    virtualBossHP -= castsBeforeNextRecharge * 2
    print(f"{virtualBossHP=}")
    virtualPlayerMana = virtualPlayerMana - (castsBeforeNextRecharge * drain.cost + recharge.cost) + 101 * 5
    print(f'{virtualPlayerMana=}')
    maxTurns += castsBeforeNextRecharge + 1
    sleep(1)

virtualBossHP = bossHP
minCastsNecessary, remain = divmod(virtualBossHP, magicMissile.dmg)
virtualPlayerMana = playerMana
minTurns = 0
while virtualBossHP > 0:
    print(f"Initial {virtualPlayerMana=}")
    castsBeforeNextRecharge = (virtualPlayerMana - recharge.cost) // magicMissile.cost
    print(f"{castsBeforeNextRecharge=}")
    virtualBossHP -= castsBeforeNextRecharge * 2
    print(f"{virtualBossHP=}")
    virtualPlayerMana = virtualPlayerMana - (castsBeforeNextRecharge * magicMissile.cost + recharge.cost) + 101 * 5
    print(f'{virtualPlayerMana=}')
    minTurns += castsBeforeNextRecharge + 1
    sleep(1)

print(f'{maxTurns=}')
print(f"{minTurns=}")


# while True:
#     pass