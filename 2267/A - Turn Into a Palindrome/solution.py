import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n,c = input().split()
    n=int(n)
    s=input().strip()
    ans=0
    for i in range(n//2):
        j=n-1-i
        if s[i]==s[j]:
            continue
        if s[i]==c or s[j]==c:
            ans += 1
        else:
            ans += 2
    print(ans)