def valid(arr):
    seen = set()
    i = 0
    n = len(arr)

    while i < n:
        v = arr[i]

        if v in seen:
            return False

        seen.add(v)

        while i < n and arr[i] == v:
            i += 1

    return True


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # Already valid
        if valid(a):
            print("YES")
            continue

        positions = []

        # Find positions where the block property is violated
        first = {}
        last = {}

        for i, x in enumerate(a):
            if x not in first:
                first[x] = i
            last[x] = i

        bad = []

        for x in first:
            for i in range(first[x], last[x] + 1):
                if a[i] != x:
                    bad.append(i)

        bad = list(set(bad))

        # More than a few bad positions => impossible
        if len(bad) > 8:
            print("NO")
            continue

        candidates = set(bad)

        for pos in bad:
            candidates.add(first[a[pos]])
            candidates.add(last[a[pos]])

        candidates = list(candidates)

        found = False

        # Try all possible swaps among candidate positions
        for i in range(len(candidates)):
            for j in range(i, len(candidates)):
                x = candidates[i]
                y = candidates[j]

                a[x], a[y] = a[y], a[x]

                if valid(a):
                    found = True

                a[x], a[y] = a[y], a[x]

                if found:
                    break

            if found:
                break

        print("YES" if found else "NO")


solve()
