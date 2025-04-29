n = int(input())
prep_arr = []
age = []
name = []
for i in range(n):
    prep_arr.append(input())
    

prep_arr.sort(key=lambda x: int(x.split(' ')[0]))

for j in range(n):
    print(prep_arr[j])
