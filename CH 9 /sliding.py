from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

pos = mc.player.getTilePos()

x,y,z = 10,11,12

x += random.uniform(-0.2, 0.2)

z += random.uniform(-50, 50)

y = mc.getHeight(x,z)

mc.player.setPos(x,y,z)
time.sleep(0.5)