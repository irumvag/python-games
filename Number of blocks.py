blocks = int(input("Enter the number of blocks: "))
height=0
sum=0
i=1
while i<=blocks:
    sum=sum+i
    if sum>blocks:
        break
    else:
        height=height+1
    i+=1
print("The height of the pyramid:", height)
# Write your code here.
#	


