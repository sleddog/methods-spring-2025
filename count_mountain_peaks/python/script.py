import sys
arguments = sys.argv[1:]

def count_mountain_peaks(elevations):
    peaks = 0
    previous = elevations[0]
    rising = False
    for elevation in elevations[1:]:
        if elevation > previous:
            rising = True
            previous = elevation
        if elevation < previous and rising == True:
            peaks += 1
            rising = False

    return peaks



if __name__ == '__main__':
    if len(sys.argv) > 1:
        elevations = list(map(int, sys.argv[1:]))
        print("elevations: ", str(elevations))
        print("peaks: ", str(count_mountain_peaks(elevations)))
    else:
        print("No elevations passed, using [4500, 7200, 6800, 8100, 7900, 9000, 8500]")
        default_elevations = [4500, 7200, 6800, 8100, 7900, 9000, 8500]
        print("peaks: " + str(count_mountain_peaks(default_elevations)))