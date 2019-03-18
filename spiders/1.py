def recursions(n):
    if n == 1:
        # 退出条件
        return 1
    # 继续递归
    return n * recursions(n - 1)


print(recursions(3))