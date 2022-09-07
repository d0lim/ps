def build_traingle(n):
    if n == 3:
        return "  *  \n * * \n*****"
    else:
        triangle = build_traingle(n // 2)
        space = " " * (n // 2)
        return (
            "\n".join(map(lambda x: space + x + space, triangle.split("\n")))
            + "\n"
            + "\n".join(map(lambda x: x + " " + x, triangle.split("\n")))
        )


N = int(input())

print(build_traingle(N))
