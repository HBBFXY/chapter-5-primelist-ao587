def PrimeList(N):
    # 用于存储小于N的质数
    primes = []
    # 遍历2到N-1的所有数
    for num in range(2, N):
        # 假设当前数是质数
        is_prime = True
        # 遍历2到num的平方根，判断是否能被整除
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        # 如果是质数，添加到列表中
        if is_prime:
            primes.append(str(num))
    # 以空格分隔输出，末尾无空格
    return ' '.join(primes)
