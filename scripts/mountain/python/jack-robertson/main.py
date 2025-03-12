def count_mountain_peaks(elevations: list[int]) -> int:
    peak_count = 0
    
    for i in range(1, len(elevations) - 1):
        if elevations[i] > elevations[i - 1] and elevations[i] > elevations[i + 1]:
            peak_count += 1

    return peak_count

print(count_mountain_peaks([4500, 7200, 6800, 8100, 7900, 9000, 8500])) 
print(count_mountain_peaks([5000, 6000, 7000, 8000]))  
