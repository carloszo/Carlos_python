def squares_even(n):
    if n>1:
        list=range(2,n+1,2)
    print([i*i for i in list])

def remove_duplicates(my_list):
    result=[]
    for i in my_list:
        if i not in result:
            result.append(i)
    print(result)

squares_even(10)
remove_duplicates([1, 3, 5, 3, 2, 2])