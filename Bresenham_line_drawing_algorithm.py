x1 = input("First point --> x1 : ")
y1 = input("First point --> y1 : ")
x2 = input("Second point --> x2 : ")
y2 = input("First point --> y2 : ")

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

dx = x2 - x1
dy = y2 - y1
ddy = dy * 2
ddx = dx * 2
k1 = ddy - ddx
p0 = ddy - dx

x = x1
y = y1
p = p0

print("P0 --> x = {} , y = {} ".format(x, y))

for iteration in range(1, 20):

    if x == x2 and y == y2:
        break
    elif p >= 0:
        x = x + 1
        y = y + 1
        p = p + k1
    else:
        x = x + 1
        p = p + ddy
    print("P{} --> x = {} , y = {} ".format(iteration, x, y))
