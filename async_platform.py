from mcpi.minecraft import Minecraft
import time
import asyncio

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()
x += 2

async def create_platform(x, y, z, distance, block_id, time_delay):
    mc.setBlocks(x, y, z, x+2, y, z+3, 35)

    ix, iy, iz = x, y, z
    while True:
        for i in range(distance):
            mc.setBlocks(ix, iy, iz, ix+2, iy, iz, 0)
            mc.setBlocks(ix, iy, iz+4, ix+2, iy, iz+4, block_id)
            iz += 1
            await asyncio.sleep(time_delay)

        for i in range(distance):
            mc.setBlocks(ix, iy, iz, ix+2, iy, iz, block_id)
            mc.setBlocks(ix, iy, iz+4, ix+2, iy, iz+4, 0)
            iz -= 1
            await asyncio.sleep(time_delay)

async def main():
    platform1 = asyncio.create_task(create_platform(x, y, z, 5, 35, 1))
    platform2 = asyncio.create_task(create_platform(x, y+2, z+2, 5, 35, 1))

    
    await platform1
    await platform2


asyncio.run(main())