from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x= pos.x
y= pos.y
z= pos.z
width = 8000
height = 8000
length= 8000
blockType = 1
air = 0
mc.setBlocks(x,y,z,x+width, y+height, z+length, blockType)
mc.setBlocks(x+1,y+1,z+1,x+width-1, y+height-1, z+length-1,air)
