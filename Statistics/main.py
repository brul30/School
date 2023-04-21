import statistics

# Define functions
def frequency(numbers, low, high):
    """
    Counts the number of values in the given list that are within the specified range.
    """
    count = 0
    for num in numbers:
        if low < num <= high:
            count += 1
    return count

def relative_frequency(count, n):
    """
    Calculates the relative frequency of a value given its count and the total number of values.
    """
    return count / n

def analyze_data(numbers):
    """
    Analyzes the given list of numbers and prints various statistics.
    """
    # Calculate basic statistics
    total_num = sum(numbers)
    mean = statistics.mean(numbers)
    median = statistics.median(numbers)
    std = statistics.stdev(numbers)
    mode = statistics.mode(numbers)
    variance = statistics.variance(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    data_range = max_val - min_val
    size_of_data = len(numbers)

    # Print basic statistics
    print(f"Sum of total numbers: {total_num}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard deviation: {std}")
    print(f"Variance: {variance}")
    print(f"Maximum value: {max_val}")
    print(f"Minimum value: {min_val}")
    print(f"Data range: {data_range}")
    print(f"Size of data set: {size_of_data}\n")

    # Read frequency ranges from file and calculate relative frequencies
    with open('frequencies.txt', 'r') as file:
        n = size_of_data
        for line in file:
            low, high = [int(num) for num in line.strip().split(',')]
            count = frequency(numbers, low, high)
            rel_freq = relative_frequency(count, n)
            print(f"There are {count} values between {low} and {high} (relative frequency: {rel_freq})")

# Define main function to run the analysis
def main():
    with open('data.txt', 'r') as file:
        numbers = [float(num) for num in file.read().split(',')]
    analyze_data(numbers)

# Run main function if this script is being executed directly
if __name__ == "__main__":
    main()

