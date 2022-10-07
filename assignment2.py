import os

game = True
error = ""

def tryAgain():
    global error, game
    os.system("clear")
    error = "\nYou entered an incorrect command. Please try again!"
    game = True

while game:
    print("""<-----RULES----->\n1. BRUSH DOWN\n2. BRUSH UP\n3. VEHICLE ROTATES RIGHT
4. VEHICLE ROTATES LEFT\n5. MOVE UP TO X\n6. JUMP\n7. REVERSE DIRECTION\n8. VIEW THE MATRIX\n0. EXIT
Please enter the commands with a plus sign (+) between them. """+error)
    inp_str = [x for x in input().split("+")]
    if len(inp_str) <= 1:
        inp_str.append("9")
    for num in inp_str[1:]:
        if num[:2] == "5_":
            try:
                y = int(num[2:])
                if y < 0:
                    num = "9"
                continue
            except:
                num = "9"
        if num not in ['0', '1', '2', '3', '4', '6', '7', '8']:
            tryAgain()
            break
        else:
            game = False
    try:
        int(inp_str[0])
        1 / int(inp_str[0][0])
    except:
        tryAgain()

size = int(inp_str[0])
arr = [["+" for y in range(size+2)] for x in range(size+2)]
for row in arr[1:-1]:
    row[1:-1] = " "*(len(row)-2)

a, b, direction, brush = 1, 1, 1, False

def paint():
    if brush:
        arr[a][b] = "*"

def updateLocation(direction, amount):
    global a, b
    if direction == 1:
        b += amount
        if b > size:
            b -= size
    elif direction == 3:
        b -= amount
        if b < 1:
            b += size
    elif direction == 2:
        a += amount
        if a > size:
            a -= size
    elif direction == 4:
        a -= amount
        if a < 1:
            a += size

def move(direction, distanceTraveled):
    for i in range(distanceTraveled):
        paint()
        updateLocation(direction, 1)
    paint()

def view():
    for i in arr:
        for j in i:
            print(j, end="")
        print("")

for cmd in inp_str[1:]:
    if cmd == "1":
        brush = True
        paint()
    elif cmd == "2":
        brush = False
    elif cmd == "3":
        direction += 1
        if direction > 4:
            direction -= 4
    elif cmd == "4":
        direction -= 1
        if direction < 1:
            direction += 4
    elif cmd[0] == "5":
        move(direction, int(cmd[2:]))
    elif cmd == "6":
        paint()
        updateLocation(direction, 3)
        brush = False
    elif cmd == "7":
        direction += 2
        if direction > 4:
            direction -= 4
    elif cmd == "8":
        view()
    elif cmd == "0":
        break
