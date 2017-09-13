def BSEARCH(L,N,Data):    
    B,E,Pos = 0,N-1,-1
    while B<=E:
        mid = (B+E)/2
        if L[mid] == Data:
            Pos = mid
            break
        if Data < L[mid]:
            E = mid-1            
        if Data > L[mid]:
            B = mid+1            
    return Pos

List = []
n = input("Enter size of list:- ")
print "Enter",n,"no. is ascending order"

for i in range(n):
    List.append(input(":- "))

print "Original List contents are:- ",List

D = input('Enter data to search:- ')
flag = BSEARCH(List,n,D)

if flag<0:
    print "Data is not present in list"
else:
    print "Data is present in list at pos ",flag +1
    
