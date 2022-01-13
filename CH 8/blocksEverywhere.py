from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
def randomBlockLocations(blockType, repeats):
    count = 0
    
    while count < repeats:
    
        x = random.randint(-127,127)
        z = random.randint(-127,127)
        y = mc.getHeight(x,z)
        mc.setBlock(x,y,                                                                                                                                                                                       z,  blockType)
        count += 1
        
randomBlockLocations(57, 10)
randomBlockLocations(1, 37)
randomBlockLocations(103, 102)