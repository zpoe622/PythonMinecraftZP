from mcpi.minecraft import Minecraft
mc =  Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x,z)
highEnough = y >=10
mc.postToChat(highestBlockY)
if highEnough==1:
    mc.postToChat("True")
else:
    mc.postToChat("False")