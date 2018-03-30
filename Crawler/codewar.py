def nb_year(p0, percent, aug, p):
    n=0
    while p0<p:
        p0=p0+p0*percent/100+aug
        n+=1
    print(n)

nb_year(1500000, 0.25, 1000, 2000000)

def divisors(integer):
    list=[2,3,4,5,6,7,8,9]
    result=[]
    for num in list:
        if integer%num==0:
            result.append(num)
    if len(result)==0:
        print(str(integer) + ' is prime')
    else:
        print(result)

divisors(18)


def is_square(n):
    return False # fix me

