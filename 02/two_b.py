"""
    This could be solved using a lambda expression and functools.reduce(),
    but the extra functions add overhead thus slowing the code down.
    Not really needed for such a simple code.
"""

def two_b():
    total = 0

    with open('two_raw.txt', 'r') as f:
        for line in f:
            array = sorted(map(int, line.split('x')))

            ribbon = 2*(array[0] + array[1])
            bow = array[0] * array[1] * array[2]

            total += ribbon + bow

    print(total)