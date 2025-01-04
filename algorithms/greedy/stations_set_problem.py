def greedy_set_stations(stations: dict[str, set[str]], states_needed: set[str]) -> set[str]:
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()

        for station, states in stations.items():
            # Find the states covered by the current station
            covered = states_needed.intersection(states)
            
            # comparison: if the current station covers more states than the previous best station,
            # update the best station and the states covered
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed = states_needed.difference(states_covered) # remove the states covered by the best station
        final_stations.add(best_station)

    
    return final_stations

if __name__ == "__main__":
    stations = dict()
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    states_needed_cov = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    best_stations = greedy_set_stations(stations, states_needed_cov)

    print(best_stations)  # {'kone', 'ktwo', 'kthree', 'kfive'}
