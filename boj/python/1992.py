import sys

N = int(sys.stdin.readline().rstrip())


def print_img(img):
    for row in img:
        print(row)


def get_area(img, area):
    l = len(img)
    if area == 0:
        return [img[i][: l // 2] for i in range(l // 2)]
    elif area == 1:
        return [img[i][l // 2 :] for i in range(l // 2)]
    elif area == 2:
        return [img[i][: l // 2] for i in range(l // 2, l)]
    elif area == 3:
        return [img[i][l // 2 :] for i in range(l // 2, l)]


def check_area(area):
    std = area[0][0]
    for row in area:
        for col in row:
            if col != std:
                return -1
    else:
        return std


def probe(img):
    c = check_area(img)
    if c != -1:
        return str(c)
    sol = ["", "", "", ""]
    areas = []
    for i in range(4):
        areas.append(get_area(img, i))
    for i in range(4):
        c = check_area(areas[i])
        if c != -1:
            sol[i] = str(c)
        else:
            sol[i] = probe(areas[i])
    return "(" + "".join(sol) + ")"


img = []
for _ in range(N):
    img.append(list(map(int, list(sys.stdin.readline().rstrip()))))

print(probe(img))
