from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def makeMelon(block,sleep,distance):
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x,y-distance,z,block)
    time.sleep(sleep)
    

count=(0)

while count < 7:
    makeMelon(103,10,1)
    count += 1