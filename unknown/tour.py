from mcpi.minecraft import Minecraft
import time
mc= Minecraft.create()
x=10
y=15
z=12
mc.player.setTilePos(x,y,z)
time.sleep(10)
x=10
y=15
z=12
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=100
y=150
z=32
mc.player.setTilePos(x,y,z)
time.sleep(10)

x=127
y=127
z=1 
mc.player.setTilePos(x,y,z)
time.sleep(10)

