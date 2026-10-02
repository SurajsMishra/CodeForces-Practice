import sys
 
input = sys.stdin.buffer.readline
 
 
def solve():
    n = int(input())
    m = 2 * n
 
    a = [None] + [
        [0] + list(map(int, input().split()))
        for _ in range(m)
    ]
 
    ans = []
 
    # ---------------------------------------------------------
    # Apply operation (i, j)
    #
    # Swap rows i and i+1 in columns j and j+1.
    # ---------------------------------------------------------
    def opr(i, j):
        a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
        a[i][j + 1], a[i + 1][j + 1] = (
            a[i + 1][j + 1],
            a[i][j + 1]
        )
        ans.append((i, j))
 
    # ---------------------------------------------------------
    # Find value x in column j, starting from row x.
    # ---------------------------------------------------------
    def wh(x, j):
        for i in range(x, m + 1):
            if a[i][j] == x:
                return i
 
        # Should never happen.
        return -1
 
    # ---------------------------------------------------------
    # Move x upward in column j+1.
    # ---------------------------------------------------------
    def R(x, j):
        pos = wh(x, j + 1)
 
        for i in range(pos - 1, x - 1, -1):
            opr(i, j + 1)
 
    # ---------------------------------------------------------
    # Handle L-R interaction.
    # ---------------------------------------------------------
    def RL(x, j):
        pos1 = wh(x, j + 1)
        pos2 = wh(x, j + 2)
 
        while pos1 > pos2:
            pos1 -= 1
            opr(pos1, j)
 
        while pos1 < pos2:
            pos2 -= 1
            opr(pos2, j + 2)
 
        while pos1 > x:
            pos1 -= 1
            opr(pos1, j + 1)
 
    # ---------------------------------------------------------
    # Move x upward in column j.
    # ---------------------------------------------------------
    def L(x, j):
        pos = wh(x, j)
 
        for i in range(pos - 1, x - 1, -1):
            opr(i, j - 1)
 
    # ---------------------------------------------------------
    # Special L-case.
    # ---------------------------------------------------------
    def L1(x, j):
        if a[x + 1][j] == x:
            opr(x + 1, j)
 
        # Extra operation, bounded by the construction.
        opr(x, j - 1)
 
        pos = wh(x, j)
 
        for i in range(pos - 1, x, -1):
            opr(i, j)
 
        opr(x, j - 1)
 
    # ---------------------------------------------------------
    # Pair has no x in its top row.
    # Put the two x's at the same depth and bring them up.
    # ---------------------------------------------------------
    def solve0(x, j):
        pos1 = wh(x, j)
        pos2 = wh(x, j + 1)
 
        while pos1 > pos2:
            pos1 -= 1
            opr(pos1, j - 1)
 
        while pos1 < pos2:
            pos2 -= 1
            opr(pos2, j + 1)
 
        while pos1 > x:
            pos1 -= 1
            opr(pos1, j)
 
    # ---------------------------------------------------------
    # Fix the first pair (columns 1,2).
    # ---------------------------------------------------------
    def lft(x):
        # If one of the two already contains x at row x,
        # handle the boundary case.
        if a[x][2] == x:
 
            if a[x][1] == x:
                return
 
            if a[x + 1][1] == x:
                opr(x + 1, 1)
 
            opr(x, 1)
 
        elif a[x][1] == x:
 
            if a[x + 1][2] == x:
                opr(x + 1, 1)
 
            opr(x, 1)
 
        pos1 = wh(x, 1)
        pos2 = wh(x, 2)
 
        if pos1 > pos2:
            while pos1 > pos2:
                pos1 -= 1
                opr(pos1, 1)
 
            pos2 += 1
 
        while pos1 < pos2:
            pos2 -= 1
            opr(pos2, 2)
 
        while pos1 > x:
            pos1 -= 1
            opr(pos1, 1)
 
    # ---------------------------------------------------------
    # Fix the last pair (columns m-1,m).
    # ---------------------------------------------------------
    def rgt(x):
        if a[x][m - 1] == x:
 
            if a[x][m] == x:
                return
 
            if a[x + 1][m] == x:
                opr(x + 1, m - 1)
 
            opr(x, m - 1)
 
        elif a[x][m] == x:
 
            if a[x + 1][m - 1] == x:
                opr(x + 1, m - 1)
 
            opr(x, m - 1)
 
        pos1 = wh(x, m - 1)
        pos2 = wh(x, m)
 
        if pos1 < pos2:
            while pos1 < pos2:
                pos2 -= 1
                opr(pos2, m - 1)
 
            pos1 += 1
 
        while pos1 > pos2:
            pos1 -= 1
            opr(pos1, m - 2)
 
        while pos1 > x:
            pos1 -= 1
            opr(pos1, m - 1)
 
    # ---------------------------------------------------------
    # Finally fix value m.
    #
    # At this point every column contains only m-1 and m
    # in the last two rows.
    # ---------------------------------------------------------
    def last():
        for j in range(1, m):
            if a[m][j] != m:
                opr(m - 1, j)
 
    # ---------------------------------------------------------
    # 1. Check total inversion parity.
    # ---------------------------------------------------------
    inv_parity = 0
 
    for j in range(1, m + 1):
        for i in range(1, m + 1):
            for k in range(i + 1, m + 1):
                if a[i][j] > a[k][j]:
                    inv_parity ^= 1
 
    if inv_parity:
        print(-1)
        return
 
    # ---------------------------------------------------------
    # Special case n = 1
    # ---------------------------------------------------------
    if n == 1:
        if a[1][1] == 2:
            print(1)
            print(1, 1)
        else:
            print(0)
        return
 
    # ---------------------------------------------------------
    # Process x = 1 ... 2n-2.
    #
    # Columns are paired:
    #
    # (1,2), (3,4), ..., (m-1,m)
    # ---------------------------------------------------------
    for x in range(1, m - 1):
 
        # -----------------------------------------------------
        # Type 1:
        # Both cells at row x contain x.
        #
        # Move both x's down temporarily.
        # -----------------------------------------------------
        for j in range(3, m - 2, 2):
            if a[x][j] == x and a[x][j + 1] == x:
                opr(x, j)
 
        # -----------------------------------------------------
        # Type L:
        # left cell is x, right cell isn't.
        # -----------------------------------------------------
        for j in range(3, m - 2, 2):
            if a[x][j] == x and a[x][j + 1] != x:
 
                if j == m - 3 or a[x][j + 3] != x:
                    R(x, j)
                else:
                    RL(x, j)
 
        # -----------------------------------------------------
        # Type R:
        # right cell is x, left cell isn't.
        #
        # Process from right to left.
        # -----------------------------------------------------
        for j in range(m - 3, 2, -2):
            if a[x][j] != x and a[x][j + 1] == x:
 
                if a[x][j - 2] == x and a[x][j - 1] == x:
                    L1(x, j)
                else:
                    L(x, j)
 
        # -----------------------------------------------------
        # Type 0:
        # Neither cell is x.
        #
        # Bring the two x's to the same depth and lift them.
        # -----------------------------------------------------
        for j in range(3, m - 2, 2):
            if a[x][j] != x:
                solve0(x, j)
 
        # Boundary pairs.
        lft(x)
        rgt(x)
 
    # ---------------------------------------------------------
    # Last value.
    # ---------------------------------------------------------
    last()
 
    # Safety check for the required bound.
    limit = n * ((m * (m - 1)) // 2) + 9 * n
 
    if len(ans) > limit:
        print(-1)
        return
 
    print(len(ans))
 
    out = []
    for i, j in ans:
        out.append(f"{i} {j}")
 
    sys.stdout.write("
".join(out) + ("
" if out else ""))
 
 
# -------------------------------------------------------------
# Main
# -------------------------------------------------------------
 
def main():
    t = int(input())
 
    for _ in range(t):
        solve()
 
 
if __name__ == "__main__":
    main()