#list=[]
#n=int(input())
#for i in range(0,n):
#    ele=int(input())
#    list.append(ele)
#list2=[]
#for i in list:
#    if i not in list2:
#        list2.append(i)

#list2.sort(reverse=False)
#print(list2[-2])

n = int(input())
string_num_as_int = input()
string_num_split = string_num_as_int.split()
nums = map(int, string_num_split)
make_a_set=set(nums)
make_a_list=list(make_a_set)
sort_the_list=sorted(make_a_list)
print(sort_the_list[-2])