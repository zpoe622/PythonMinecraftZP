from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x=0
y=0
z=0
gift = mc.getBlock(x,y,z)
if gift!=0:
    if gift!=57:
        mc.setBlock(-1-2,0, 10)
    else:
        mc.setBlock(1,0,1,0)
else:
    mc.postToChat("Place an offering on the pedastal.")