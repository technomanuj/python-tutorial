# import user defined module
from mymodule import *
# import mymodule as mm

neon = 5
print('Factorial of {0} is'.format(neon), fact(neon))

print("Name with maximum five characters", morethanfive("manoj", "anuj", "tanuj", "kaka", "rajkishore"))

print("Total name have more than five characters", name_gt_five_char("manoj", "anuj", "tanuj", "kaka", "rajkishore"))
