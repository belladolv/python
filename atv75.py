fibonacci = [1, 1]
for i in range(2, 15):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)
