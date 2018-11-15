ones=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens=["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
def cal(x):
    if x<20:
        return len(ones[x-1])
    if x>=20 and x<100:
        return len(tens[x//10-2])+(cal(x%10) if x%10>0 else 0)
    if x>=100 and x<1000:
        return len(ones[x//100-1])+7+(cal(x%100)+3 if x%100>0 else 0)
sum=0
for i in range(1,1000):
    print(i,"=",cal(i),end=" ")
    print("\n")
    sum=sum+cal(i)
print(sum+11)



