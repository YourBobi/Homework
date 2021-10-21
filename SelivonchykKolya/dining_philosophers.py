import threading
from time import sleep

count_philosophers = 5
count_forks = 5
forks = [threading.Lock() for i in range(count_forks)]
philosophers = [i for i in range(count_philosophers)]


def eating(f1, index, f2):
    print(f"Philosopher {philosophers[index]} start to eat!")
    sleep(3)
    print(f"Philosopher {philosophers[index]} finished eat!")
    f1.release()
    f2.release()


def dinning_philosophers():
    i = 0
    while True:
        f1 = forks[i % count_forks]
        number_of_philosopher = i % count_forks
        f2 = forks[(i + 1) % count_forks]

        if not f1.locked() and not f2.locked():
            f1.acquire(blocking=True)
            f2.acquire(blocking=True)
            threading.Thread(target=eating, args=[f1, number_of_philosopher, f2]).start()

        i += 1


if __name__ == "__main__":
    dinning_philosophers()
