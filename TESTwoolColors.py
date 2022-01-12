from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 35
state = 6
#makes pink wool
mc.setBlock(10, 3, -4, block, state)
mc.setBlocks(11, 3, -4, 20, 6, -8, block, state)