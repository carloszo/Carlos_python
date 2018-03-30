#!/usr/bin/python
#-*- coding:utf8 -*-
import multiprocessing as mp
#   学习多进程的使用方法
def job(a,b):
    print('aaaaa')

#queue的使用
def job2(q):
    res = 0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)

def job3(x):
    return x*x



if __name__=='__main__':
    # m1 = mp.Process(target=job,args=(1,2))
    # m1.start()
    # m1.join()
    #q=mp.Queue()
    '''
    m1=mp.Process(target=job2,args=(q,))
    m2=mp.Process(target=job2,args=(q,))
    m1.start()
    m2.start()
    m1.join()
    m2.join()
    res1=q.get()
    res2=q.get()
    print(res1+res2)
    '''
    # pool
    #map()可以放入多个参数
    #自定义核数量方法：pool = mp.Pool(processes=2)

    pool = mp.Pool()
    res=pool.map(job3,range(10))
    print(res)
    #apply_async(),只能传人一个值并返回一个结果,返回值需用get()获取
    res1=pool.apply_async(job3,(100,))
    print(res1.get())
    # apply_async()返回多个结果可采用迭代器
    multi_res=[pool.apply_async(job3,(i,)) for i in range(10)]
    #同样值也要一个一个取出来
    print([res.get() for res in multi_res])
