import sys
arguments = sys.argv[1:]
    
def count_mountain_peaks(elevations: list[int]) -> int:
    peak_count = 0
    
    for i in range(1, len(elevations) - 1):
        if elevations[i] > elevations[i - 1] and elevations[i] > elevations[i + 1]:
            peak_count += 1

    return peak_count

result = count_mountain_peaks(arguments)
print(result)
