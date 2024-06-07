# from threading import Thread
# from time import sleep


# def first():
#   for _ in range(10):
#     print(1)

# def second():
#   for _ in range(10):
#     print(2)

# thread_1 =  Thread(target=first)
# thread_2 =  Thread(target=second)

# thread_1.start()
# thread_2.start()

# print(333)

# thread_1.join()
# thread_2.join()





import asyncio

async def first():
  for _ in range(10):
    print(1)
    await asyncio.sleep(0.1)

async def second():
  for _ in range(10):
    print(2)
    await asyncio.sleep(0.1)




if __name__ == "__main__":
  asyncio.run(first())
  asyncio.run(second())

