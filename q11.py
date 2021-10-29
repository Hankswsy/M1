x = str(input())
y = []

for i in range(len(x)):
    y.append((int(x[i])+7)%10)

print(f"{y[2]}{y[3]}{y[0]}{y[1]}\n")

    