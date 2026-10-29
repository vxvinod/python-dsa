import requests
import asyncio

BASE_URL = "https://dummyjson.com/users"

async def fetch_user(user_id: int):
    try:
        response = requests.get(f"{BASE_URL}/{user_id}")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Exception raised {e}")

async def fetch_users_async(user_id: int):
    return await fetch_user(user_id)

async def main():
    user_ids = range(1,6)
    results = await asyncio.gather(*(fetch_users_async(uid) for uid in user_ids))
    for r in results:
        print(r["id"], r["firstName"])


if __name__ == "__main__":
    asyncio.run(main())