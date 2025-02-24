import random, os, time

os.system('cls | clear')

WIDTH = os.get_terminal_size()[0] - 1
MIN_TRAIL_LEN = 5

try:
    while True:
        trail_length = random.randint(MIN_TRAIL_LEN, WIDTH - 70)
        for i in range(trail_length):
            print('❄️' * i + '⛄️', end='', flush=True)
            time.sleep(3 / trail_length)  # Use 0.9 instead of 1.0 because printing adds a delay and I want it to be roughly 1 second per snail.
            print('\b' * (i + 1), end='', flush=True)
        print('🧊' * trail_length + '⛄️🛑🚓', end='', flush=True)

        print('\n' * random.randint(1, 6))

except KeyboardInterrupt:
    print('Frosty in the Metaverse, inspired by Snail Trail, by Al Sweigart al@inventwithpython.com 2024')