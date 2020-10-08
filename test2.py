n=int(input("수 : "))
i=1
sum=0

while i <= n :
    sum=sum+i
    i=i+1

print("1부터",n,"까지의 합은 :",sum)

if (n==0):
    print("프로그램을 종료합니다.")
