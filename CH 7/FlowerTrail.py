from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while true
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 35)
    time.sleep(.2)