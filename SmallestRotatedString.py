def get_smallest_word(string, k):
    string = list(string)

    if k == 1:
        best = string
        for i in range(1, len(string)):
            if string[i:] + string[:i] < best :
                best = string[i:] + string[:i]
        return ''.join(best)

    else:
        return ''.join(sorted(string))

def main():
    print(get_smallest_word('daily', 2))

if __name__ == "__main__":
    main()