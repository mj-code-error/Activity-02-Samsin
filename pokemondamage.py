import random

target = 1
weather = 1
badge = 1
stab = 1
other = 1
type = 1
critical = random.randint(1, 2)
rdom = round(random.uniform(0.85, 1.00), 2)

burn = random.randint(0, 1)
if burn == 0:
    burn = 0.5
else:
    burn = 1

modifiers = (target * weather * badge * critical * rdom * stab * type * burn * other)

level = 90
power = 110
ATK = 205
DEF = 188

Damage = ((((2 * level / 5) + 2) * power * (ATK / DEF) / 50) + 2) * float(modifiers)

print(Damage)