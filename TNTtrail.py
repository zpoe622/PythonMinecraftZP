from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
while True:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 46, 1)
    time.sleep(.2)