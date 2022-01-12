from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x=0
y=0
z=0
melon=103
noMelon = mc.getBlock(x,y,z)
noMelon= noMelon!=103
mc.postToChat("You need to get some food: "+str(noMelon))