##week14-1.py CPE 2026/05/26:Minesweeper
t=1
while True:
    m,n=list(map(int,input().split()))
    if m==0 and n==0: break
    a=[]
    for i in range(m):
        a.append(list(input()))
    for i in range(m):
        for j in range(n):
            if a[i][j]=='*': continue
            a[i][j]=0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if ii<0 or jj<0 or ii>=m or jj>=n:
                        continue
                    if a[ii][jj]=="*":
                        a[i][j]+=1
    if t>1: print()
    print(f'Field #{t}:')
    for i in range(m):
        for j in range(n):
            print(a[i][j],end='')
        print()
    t+=1
