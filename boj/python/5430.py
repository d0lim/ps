import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr_str = sys.stdin.readline().rstrip().strip("[").strip("]").split(",")
    arr = list(map(int, arr_str)) if arr_str != [""] else []
    # arr = eval(sys.stdin.readline().rstrip())
    # cmd.replace("RR", "")
    r = False
    err = False
    for c in cmd:
        if c == "D":
            if len(arr) == 0:
                print("error")
                err = True
                break
            if r:
                arr.pop(-1)
            else:
                arr.pop(0)
        elif c == "R":
            r = not r
    if not err:
        if r:
            print("[" + ",".join(map(str, arr[::-1])) + "]")
        else:
            print("[" + ",".join(map(str, arr)) + "]")
