def get_manhattan_distance((coord1), (coord2)):
    dist = 0;
    dist = abs(coord2[0]-coord1[0])+abs(coord2[1]-coord1[1])
    return dist
