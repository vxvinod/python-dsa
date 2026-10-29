from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False

    return True

NUMBERS = [100_000_000000000000000000000000000000000000000000000000000_000_002 + i for i in range(8)]

def run_sequential():
    start = time.perf_counter()
    results = [is_prime(n) for n in NUMBERS]
    print(f"sequential time - {time.perf_counter() - start}--results-{results}")


def run_process_pool():
    start = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(is_prime, NUMBERS))
    print(f"process pool exeuction {time.perf_counter() - start}--results --{results}")


def run_thread_pool():
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(is_prime, NUMBERS))
    print(f"thread pool executor - {time.perf_counter() - start}--results --{results}")


if __name__ == "__main__":
    run_sequential()
    run_process_pool()
    run_thread_pool()