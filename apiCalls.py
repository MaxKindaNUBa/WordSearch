import asyncio
import aiohttp
from random import randint


def get_tasks(session,min,max,num):
    tasks = []
    for i in range(num):
        tasks.append(session.get(f"https://random-word-api.herokuapp.com/word?length={randint(min,max)}&lang=en"))
    return tasks


async def get_words(min,max,num):
    words = []
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,min,max,num)
        responses = await asyncio.gather(*tasks)

        for i in responses:
            words += await i.json()

    return words

print(get_words(5,20,20))