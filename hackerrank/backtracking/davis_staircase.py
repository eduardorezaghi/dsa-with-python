import functools


def stepPerms(n: int):
    # Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time.
    # Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.
    # Given the respective heights for each of the s staircases in his house, find and print the number of ways he can climb each staircase on a new line.
    # For example, there is s = 1 staircase in the house that is n = 5 steps high. Davis can step on the following sequences of steps:
    # 1. 1, 1, 1, 1, 1
    # 2. 1, 1, 1, 2
    # 3. 1, 1, 2, 1
    # 4. 1, 2, 1, 1
    # 5. 2, 1, 1, 1
    # 6. 1, 2, 2
    # 7. 2, 1, 2
    # 8. 2, 2, 1
    # 9. 1, 1, 3
    # 10. 1, 3, 1
    # 11. 3, 1, 1
    # 12. 2, 3
    # 13. 3, 2
    # There are 13 possible ways he can take these 5 steps.
    # Function Description
    # Complete the stepPerms function in the editor below. It should recursively calculate and return the integer number of ways Davis can climb the staircase, modulo 10000000007.
    # stepPerms has the following parameter(s):
    # n: an integer, the number of stairs in the staircase
    # Input Format
    # The first line contains a single integer, s, the number of staircases in his house.
    # Each of the following s lines contains a single integer, n, the height of staircase i.
    # Constraints
    # 1 <= s <= 5
    # 1 <= n <= 36
    # Output Format
    # For each staircase, return the number of ways Davis can climb it as an integer.
    
    # Approach:
    # 1. If n = 1, return 1
    # 2. If n = 2, return 2
    # 3. If n = 3, return 4
    # 4. If n > 3, return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)
    # 5. Use memoization to avoid recomputation

    @functools.lru_cache(maxsize=None)
    def stepPermsHelper(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        return stepPermsHelper(n - 1) + stepPermsHelper(n - 2) + stepPermsHelper(n - 3)
    
    return stepPermsHelper(n)

if __name__ == '__main__':
    print(stepPerms(1))  # 1
    print(stepPerms(3))  # 4
    print(stepPerms(7))  # 44
    print(stepPerms(5))  # 13
    print(stepPerms(8))  # 81
    print(stepPerms(10))  # 274
    print(stepPerms(15))  # 5768
    print(stepPerms(20))  # 121415
    print(stepPerms(25))  # 2555757
    print(stepPerms(30))  # 53798080
    print(stepPerms(35))  # 1132436852	
    print(stepPerms(36))  # 2082876103