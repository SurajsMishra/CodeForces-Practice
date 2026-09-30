import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    results = []
    idx = 1
    for  i in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx+1])
        idx += 2
        ans = (1<<(n-k+1))+2*(k-1)
        results.append(str(ans))
    print('
'.join(results))
if __name__ == '__main__':
    solve()