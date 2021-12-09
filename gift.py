from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=0
y=0
z=0
gift = mc.getBlock(x,y,z)

if gift==57:
    mc.postToChat("Thanks for the diamonds")
elif gift==6:
    mc.postToChat("I guess tree saplings are as good as diamods...")
else:
    mc.postToChat("bring a gift to" +str(x) +","+str(y)+","+str(z))