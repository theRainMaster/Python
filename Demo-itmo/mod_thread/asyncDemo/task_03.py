"""
"""
import asyncio

async def my_coro(n): 
    print(f"The answer is {n}.")

async def main(): 
    """ Создав задачу, вы запланировали ее запуск
        по усмотрению цикла событий """
    mytask = asyncio.create_task(my_coro(42))
    """программа останавливается
       пока задача не будет завершена"""
    await mytask

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


asyncio.run(main()) # 3.7+

