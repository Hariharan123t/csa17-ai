import itertools

def calculate_distance(cities, tour):
    distance = 0
    for i in range(len(tour) - 1):
        distance += cities[tour[i]][tour[i + 1]]
    distance += cities[tour[-1]][tour[0]]
    return distance

def tsp_brute_force(cities):
    num_cities = len(cities)
    all_tours = itertools.permutations(range(num_cities))
    min_distance = float('inf')
    best_tour = None
    for tour in all_tours:
        distance = calculate_distance(cities, tour)
        if distance < min_distance:
            min_distance = distance
            best_tour = tour
    return best_tour, min_distance

if __name__ == "__main__":
    cities = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    best_tour, min_distance = tsp_brute_force(cities)
    print("Best tour:", best_tour)
    print("Minimum distance:", min_distance)
