import sys

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    if m < n: # if m < n speed is faster - O(min(n, m)) 
        return edit_distance(s2, s1)

    prev = list(range(n + 1))
    for i, ch1 in enumerate(s1, 1):
        cur = [i]
        for j, ch2 in enumerate(s2, 1):
            cur.append(min(cur[-1] + 1,
                           prev[j] + 1,
                           prev[j - 1] + (ch1 != ch2)))
        prev = cur

    return prev[n]


def main():
    s1 = sys.stdin.readline()
    s2 = sys.stdin.readline()
    print(edit_distance(s1, s2))


if __name__ == '__main__':
    main()
    