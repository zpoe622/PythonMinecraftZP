
import time
from mcpi.minecraft import Minecraft
mc= Minecraft.create()

pos1 = mc.player.getTilePos()
x1=pos1.x
y1=pos1.y
z1=pos1.z

time.sleep(10)

pos2 = mc.player.getTilePos()
x2=pos2.x
y2=pos2.y
z2=pos2.z

xDistance = x2-x1
yDistance= y2-y1
zDistance = z2-z1


mc.postToChat(xDistance+yDistance+zDistance)