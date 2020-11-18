n = int(input().strip())
if (n%2!=0):
    print("Weird")
if n%2==0 and n<=20:
    if 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
if n%2==0 and n>20:
        print("Not Weird")