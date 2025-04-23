strNum = input()
# strNum = str(num)

arr = []

for i in strNum:
    arr.append(i)

# sort 함수사용 (역순)
arr.sort(reverse=True)

result = ''.join(map(str, arr))
print(result) 
