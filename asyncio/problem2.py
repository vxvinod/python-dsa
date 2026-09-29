import asyncio
import time

async def task(name, delay):
    print(f"Start task--#{name}")
    await asyncio.sleep(delay)
    print(f"End Task --#{name}")


async def main():
    start = time.time()
    await asyncio.gather(
        task("A", 5),
        task("B", 3)
    )
    print(f"Total time taken - #{time.time() - start}")


asyncio.run(main())

# Start task--#A
# Start task--#B
# End Task --#B
# End Task --#A
# Total time taken - #5.004173755645752