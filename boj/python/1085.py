import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

row_fast = x if w - x > x else w - x
col_fast = y if h - y > y else h - y

print(row_fast if row_fast < col_fast else col_fast)