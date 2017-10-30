# read_spaced_data.py
import time_series_read
def find_largest(line):
    """ (str) -> int
    Return the largest value in line, which is a whitespace-delimited string
    of integers that each end with a '.'.
    >>> find_largest('1. 3. 2. 5. 2.')
    5
    """

    # Set the largest value, to be replaced no matter what.
    largest = -1
    for value in line.split():
        # Remove the trailing period.
        v = int(value[0:-1]) # I added a zero, from first to last
        # If we find a larger value, remember it.
        if v > largest:
            largest = v

    return largest

def process_file(reader):
    """ (file open for reading) -> int
    Read and process reader, which must start with a time_series header.
    Return the largest value after the header. There may be multiple pieces
    of data on each line.
    """

    line = time_series_read.skip_header(reader).strip()

    # The largest value so far is the largest on this first line of data.
    largest = find_largest(line)

    # Check the rest of the lines for larger values.
    for line in reader:
        large = find_largest(line)
        if large > largest:
            largest = large

    return largest

if __name__ == '__main__':
    with open('lynx.txt', 'r') as input_file:
        process_file(input_file)