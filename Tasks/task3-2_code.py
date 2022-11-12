from sys import stdin
n, k = map(int, stdin.readline().split())
# 배열에 저장
# lists = [list(map(int, input().split())) for _ in range(n)]
lists = [[int(x)for x in stdin.readline().split()] for y in range(n)]


def findk(lists, startr, startc, lastr, lastc, k):

    if startr == lastr or startc == lastc:
        if lists[startr][startc] == k:
            return (startr, startc)
        else:
            return (-1, -1)

    row_m = (startr+lastr)//2
    clm_m = (startc+lastc)//2

    if k == lists[row_m][clm_m]:
        return (row_m, clm_m)
    elif k == lists[row_m+1][clm_m+1]:
        return (row_m+1, clm_m+1)

    elif k < lists[row_m][clm_m]:
        FB = findk(lists, startr, startc, row_m, clm_m, k)
        FA = findk(lists, startr, clm_m+1, row_m, lastc, k)
        FC = findk(lists, row_m+1, startc, lastr, clm_m, k)

        if FB != (-1, -1):
            return FB
        elif FA != (-1, -1):
            return FA
        elif FC != (-1, -1):
            return FC
        else:
            return (-1, -1)

    elif k > lists[row_m+1][clm_m+1]:

        FC = findk(lists, row_m+1, startc, lastr, clm_m, k)
        FA = findk(lists, startr, clm_m+1, row_m, lastc, k)
        FD = findk(lists, row_m+1, clm_m+1, lastr, lastc, k)

        if FC != (-1, -1):
            return FC
        elif FA != (-1, -1):
            return FA
        elif FD != (-1, -1):
            return FD
        else:
            return (-1, -1)

    elif lists[row_m][clm_m] < k and k < lists[row_m+1][clm_m+1]:
        FC = findk(lists, row_m+1, startc, lastr, clm_m, k)
        FA = findk(lists, startr, clm_m+1, row_m, lastc, k)
        if FC != (-1, -1):
            return FC
        elif FA != (-1, -1):
            return FA
        else:
            return (-1, -1)


print(findk(lists, 0, 0, n-1, n-1, k))
