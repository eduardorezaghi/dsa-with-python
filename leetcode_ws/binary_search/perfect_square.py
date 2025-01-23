import functools


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False

        L, R = 0, num
        while L <= R:
            mid = (L + R) // 2
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                L = mid + 1
            else:
                R = mid - 1
        return False
6
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    perfect_squares_upto_1000 = [i*i for i in range(1, 32)]


    s = Solution()
    for n in numbers:
        print(s.isPerfectSquare(n))
    for n in perfect_squares_upto_1000:
        print(s.isPerfectSquare(n))