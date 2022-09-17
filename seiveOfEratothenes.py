#This is used to find all the prime number present between 1 to n
class PrimeNumbers():
    def prime(self, n):
        array=[True]*(n+1)
        array[0]=False
        array[1]=False

        for i in range(2,int(n**(0.5))+1):
            if array[i]==False:
                continue
            for j in range(2*i,n+1,i):
                array[j]=False
        
        return array


num=int(input("Enter a number ="))

p=PrimeNumbers()
itr=0
for i in p.prime(num):
    if i:
        print(itr,end=" ")
    itr+=1

