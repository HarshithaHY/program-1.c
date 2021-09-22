def get_sum(*arrguments):
result=0;
for i in arrguments:
  result += i
  return result


print(get_sum(1,2,3))  #6
print(get_sum(1,2,3,4,5))  #15
print(get_sum(1,2,3,4,5,6,7))   #27
