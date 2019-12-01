from sys import stdin, stdout
def window(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
    
    for i in range(n - 1, -1, -1):
        min_seen = min(min_seen, array[i])
        if min_seen < array[i]:
            left = i

    return left, right

def main():
    n = stdin.readline()
    arr = [ int(x) for x in stdin.readline().split()]
    left, right = window(arr)
    stdout.write(str(left) + " " + str(right))

if __name__ == "__main__":
    main()


