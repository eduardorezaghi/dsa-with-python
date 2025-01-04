def numRescueBoats(people: list[int], limit: int) -> int:

    people.sort()
    l = 0
    r = len(people) - 1

    boats = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1

        r -= 1
        boats += 1

    return boats

if __name__ == "__main__":
    people = [3,5,3,4]
    limit = 5
    print(numRescueBoats(people, limit)) # 4
