import asyncio
import time

async def task(name, delay):
    print(f"Start of the task #{name}")
    await asyncio.sleep(delay)
    print(f"End of the task #{name}")

async def main():
    start = time.time()
    await task("A", 2)
    await task("B", 2)
    print(f"Total Time - #{time.time() - start}")


asyncio.run(main())

# Start of the task #A
# End of the task #A
# Start of the task #B
# End of the task #B
# Total Time - #3.0024428367614746

