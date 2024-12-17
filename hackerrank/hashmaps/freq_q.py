def freq_queries(queries: list[list[int]]) -> None:
    seen_elements = dict()
    output = []
    
    for operation,element in queries:
        # do something.
        match operation:
            case 1: # insert
                if element in seen_elements:
                    seen_elements[element] += 1
                else:
                    seen_elements[element] = 1

            case 2: # delete
                if element in seen_elements:
                    seen_elements[element] -= 1

                    if seen_elements[element] == 0:
                        del seen_elements[element]

            case 3: # check if element is in seen_elements
                if element in seen_elements.values():
                    output.append(1)
                else:
                    output.append(0)
            case _:
                print(0)

    print(output)
    return output

if __name__ == "__main__":
    queries = [(1,1), (2,2), (3,2)]
    freq_queries(queries)  # will print 0
    
    queries = [(1,1), (1,1), (3,2)]
    freq_queries(queries)  # will print 1
    
    queries = [(1,5), (1,6), (3,2), (1,10), (1,10), (1,6), (2,5), (3,2)]
    freq_queries(queries)  # returns [0, 1]