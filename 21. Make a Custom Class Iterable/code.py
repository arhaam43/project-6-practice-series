#       21. Make a Custom Class Iterable

# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start  # Starting point set kar diya

    def __iter__(self):
        return self  # Iterator ban gaya

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Jab 0 se neeche ho jaaye to stop karo
        val = self.current
        self.current -= 1
        return val

cd = Countdown(5)

for num in cd:
    print(num)