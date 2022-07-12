ls = [1,2,4,5,6,7,8,9]  
target = 11 
result = []
for i in range(len(ls)):
    for j in range(len(ls)):
        sum = ls[i] + ls[j] 
        if sum == target:
            result += [[i,j]]
print(result) 
