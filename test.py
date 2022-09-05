from nbt import region
import pymapper
from bitstring import *
#Load region file
regionfile = region.RegionFile("r.0.0.mca",'rb')

test = pymapper.section_data(regionfile.get_chunk(0, 0)["sections"][1])

#test = BitArray(pymapper.dump_section(regionfile.get_chunk(0, 0)["sections"][1]))
#print([test[i:i+64] for i in range(0, len(test), 64)])
x = 0
y = 0
z = 0

#x = x ^ 1
#y = y ^ 1
#z = z ^ 1

#print(test[x+(z*16)+(y*256)])
#print(test.index("minecraft:deepslate_diamond_ore"))
#print(test)
#x,y,z
#x,z,y
#y,x,z
#y,z,x
#z,y,x
#z,x,y