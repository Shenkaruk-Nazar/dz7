def reverse_number_generator():
    for number in range(10, 0, -1):
        yield number


for num in reverse_number_generator():
    print(num)


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.data:
            raise StopIteration
        value = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return value

list = Iterator([1, 2, 3, 4])

for _ in range(10):
    print(next(list))


def number1():
    for number2 in range(1, 6):
        yield (number2, number2 ** 2)

for num1, ddd in number1():
    print(f' {num1}, {ddd}')


class ssss:
    def __init__(self, value):
        self.value = value

    def dsds(self):
        def dddd(increment):
            self.value += increment
            return self.value
        return dddd


sss = ssss(10)
ss = sss.dsds()

print(ss(5))
print(ss(3))

