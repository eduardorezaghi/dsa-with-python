# Greedy algorithms are used for optimization problems.
# An optimization problem can be solved using greedy algorithms if the problem has the following properties:
# 1. Greedy-choice property: A global optimum can be arrived at by selecting a local optimum.
# 2. Optimal substructure: An optimal solution to the problem contains optimal solutions to the subproblems.
#

# Greedy problem: Activity selection problem.
# Given a set of activities with start and finish times, we want to find a subset of activities that do not overlap.
# The greedy choice is to always pick the next activity whose finish time is least among the remaining activities.



def activity_selection(start: list[int], finish: list[int]) -> list[int]:
    n = len(start)
    # Sort the activities by their finish times
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [0]
    i = 0
    for j in range(1, n):
        first_activity = activities[i][1]
        second_activity = activities[j][0]
        # Here's the greedy choice: always pick the next activity whose finish time is least among the remaining activities
        # if the start time of the next activity is greater than or equal to the finish time of the current activity
        if second_activity >= first_activity:
            selected.append(j)
            # reset the index to the next activity
            i = j
    return selected
    
    
if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print(activity_selection(start, finish))  # [0, 1, 3, 4]
    print("All tests passed")