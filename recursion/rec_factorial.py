def rec_factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * rec_factorial(n - 1)
    
if __name__ == '__main__':
    print(rec_factorial(5))  # 120
    print(rec_factorial(3))  # 6
    print(rec_factorial(1))  # 1
    print(rec_factorial(0))  # 1
    print(rec_factorial(10))  # 3628800
    print(rec_factorial(20))  # 2432902008176640000
    print(rec_factorial(50))  # 30414095443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000