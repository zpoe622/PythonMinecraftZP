import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
mc = minecraft.Minecraft.create()
mc.postToChat('Welcome to the Lava Trap')
sleep(3)
pos = mc.player.getTilePos()
mc.setBlocks(pos.x-5, pos.y-2, pos.z-5, pos.x+5, pos.y-2, pos.z+5, block.STONE.id)
mc.setBlocks(pos.x-5, pos.y-1, pos.z-5, pos.x+5, pos.y-1, pos.z+5, block.LAVA.id)
mc.setBlock(pos.x, pos.y-1,pos.z,block.DIAMOND_BLOCK.id)
mc.postToChat("Get READDDDDDYYYYYYY!!!!!!!!!!!!!!!!!!!!")
mc.postToChat("BLOCKS UNDER YOU WILL KEEP GETTING GONE UNLESS U GET SMRT")
sleep(3)
mc.postToChat("GoGoGoGoGooooooooooooooooooooooooooooooooooooooo BOIIIIIIII")
gameover=False
while gameover == False:
    p = mc.player.getTilePos()
    mc.setBlock(p.x, p.y-1, p.z, block.OBSIDIAN.id)
    sleep(0.2)
    mc.setBlock(p.x, p.y-1, p.z, block.LAVA.id)
    sleep(0.1)
    