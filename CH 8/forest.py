from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
def growTree(x,y,z):

    
    
    
    mc.setBlocks(x,y,z,x,y+6,z,17)
    mc.setBlocks(x-2,y+7,z-2,x+2,y+7,z+2,18)
growTree(x + 1, y,z)
