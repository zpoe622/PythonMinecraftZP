from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103

#BLOCK IDS
#water=9
#lava=11
#wool=35-35.15
#TNT=46
#flower=37
#diamond-blk=57

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)

