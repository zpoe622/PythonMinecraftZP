from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

blocks = []

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hit[0]
        hitX, hitY, hitZ = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(hitX, hitY, hitZ)
        blocks.append(block)
        
    if block = 56
        mc.postToChat("You found some diamond ore!!!")
    
    time.sleep(0.2)