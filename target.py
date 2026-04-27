arr = [1, 3, 5, 6]
target = 4
for i in range(len(arr)):
    if target <= arr[i]:
        print("Insert position:", i)
        break
else:
    print("Insert position:", len(arr))
