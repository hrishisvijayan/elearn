
# arr = [100, 80, 60, 70, 60, 75, 85]
# print('1')
# for i in range(1,len(arr)):
#     count = 1
#     j=i - 1
#     while arr[j] < arr[i]:
#         count += 1
#         j -= 1
#     print(count)





# count=1
# for i in range(1,8):
#     j = 0
#     max = arr[j]
#     if max > arr[i] :
#         count = count+1
#     else:
#         number = count
#         b[j] = number
#         j = j+1


a = [100, 80, 60, 70, 60, 75, 85]
ans = []        
def checker(i,span):
    if a[i-span] < a[i] and i>=span:
        span = span + 1
        checker(i,span)
    else:
        ans.append(span)
for i in range(len(a)) :
    span = 1 
    checker(i,span)

print(ans)


