M , m = input(), set(map(int,input().split()))
N , n = input(), set(map(int,input().split()))
print(*sorted(list(m.symmetric_difference(n))),sep='\n')