from django.shortcuts import render
#coding:utf8
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'你好，Carlos')

# Create your views here.
def home(request):
    #显示字符串到home.html
    # string='主持公司重大项目分析与设计,项目进度控制与质量监督;对技术部门的经费预算和费用控制;制定部门年度发展计划;协助人事部招聘部门人员;对部门人员进行考核;向总裁汇报工作进展情况;协调技术部门于其他部门及合作机构的协作.'
    # return render(request,'home.html',{'string':string})
    #list输出
    # list=['a','b','c','d']
    # return render(request,'home.html',{'list':list})
    #字典输出
    # dict={
    # '姓名':'王传喜',
    # '性别':'男',
    # '出生日期':'1976 - 01 - 01',
    # '工作年限':'10年以上',
    # '现居住地':'上海 - 上海市',
    # '学历':'硕士研究生',
    # '学位':'硕士',
    # '毕业时间':'2002 - 03 - 01',
    # '大学':'南京航空航天大学'
    # }
    # return render(request,'home.html',{'dict':dict})
    # list=range(100)
    # return render(request,'home.html',{'list':list})
    num=100
    return render(request,'home.html',{'num':num})