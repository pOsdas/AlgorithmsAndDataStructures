import random

data = []
for i in range(10):
    data.append(random.randint(-10, 10))

data.sort()
print(data)

value = int(input("Введите искомое число: "))

low = 0
high = len(data) - 1
mid = len(data) // 2

while data[mid] != value and low <= high:
    if value > data[mid]:
        low = mid + 1
    elif value < data[mid]:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Нет значения")
else:
    print(mid)
