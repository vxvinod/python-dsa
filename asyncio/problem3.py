import asyncio
import time

async def task(name, delay):
    print(f"Start task - #{name}")
    await asyncio.sleep(delay)
    print(f"End task - #{name}")
    return f"{name} task"

async def main():
    start = time.time()
    t1 = asyncio.create_task(task("A", 2))
    t2 = asyncio.create_task(task("B", 1))
    print("Both tasks created — doing other work now")
    await asyncio.sleep(0.5)
    print("Other work finished")
    result_t1 = await t1
    result_t2 = await t2
    print(result_t1, result_t2)

asyncio.run(main())

# Both tasks created — doing other work now
# Start task - #A
# Start task - #B
# Other work finished
# End task - #B
# End task - #A
# A task B task