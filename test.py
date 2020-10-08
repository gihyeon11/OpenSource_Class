def findPrime(x,y):
    print(x,"부터",y,"사이의 소수 :", end=' ')
    count=0

    for a in range(x,y+1) :
        for b in range(2,int(x/2)) :
            if a % b ==0 :
                break

        else :
            print(a,end=' ')
            count=count+1
    else :
        print()

        return count


num1=1
num2=int(input("정수 값 : "))

count=findPrime(1,num2)

print("소수는 모두",count,"개 입니다.")
