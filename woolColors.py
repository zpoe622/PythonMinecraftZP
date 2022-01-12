from mcpi.minecraft import Minecraft
mc = Minecraft.create()
block = 35
state = 6 #the different number is a different color
def getWoolState(color):
    if color == "pink":
        blockState = 6
        
    elif color == "blue":
        blockState = 11
        
    elif color == "yellow":
        blockState = 4
        
    elif color == "green":
        blockState = 13
        
    elif color == "brown":
        blockState = 12
             
    elif color == "black":
        blockState = 15
        
       
mc.setBlock(10, 3, -4, block, state)
mc.setBlocks(11, 3, -4, 20, 6, -8, block, state)