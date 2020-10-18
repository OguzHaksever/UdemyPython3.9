data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

for index in range(len(data) - 1, - 1, - 1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

print(data)

# For clearing outlying data from a list
print(
)
print("--- REVERSED FUNCTION ---"*60)
print()
top_index = len(data) - 1  # sırayı 12den çıkarmak için,
# her listle çalışsın diye direk 12den çıkarılmadı
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)



