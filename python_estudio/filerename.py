#-*- coding:utf8 -*-
import os,re
# files = os.listdir('/Users/apple/downloads')
# filenames=[]
# for file in files:
#     filenames = filter(lambda file:file[-4:]=='.jpg',files)
# #print(filenames)
# for file in filenames:
#     print(file)

film_list=[
    '[电影天堂-www.dy2018.net]铁甲钢拳BD中英双字.rmvb',
    '[阳光电影www.ygdy8.com].变形金刚5：最后的骑士.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].超速驾驶.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].荡寇风云.BD.720p.国粤双语中字.mkv',
    '[阳光电影www.ygdy8.com].生死之墙.BD.720p.中英双字幕.mkv',
'[阳光电影www.ygdy8.com].王牌保镖.BD.720p.中英双字幕.mkv',
'[阳光电影www.ygdy8.com].嫌疑人X的献身.HD.720p.国语中字.mkv',
'[阳光电影www.ygdy8.com].心理罪.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.net]寻夢環游记.HD.720p.国英双语中字.mkv',
    '[阳光电影www.ygdy8.net]奇迹男孩.HD.720p.中英双字幕.rmvb',
    '[阳光电影www.ygdy8.net].追龙.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.net].英伦对决.HD.720p.国英双语.中英双字幕.mkv',
    '[阳光电影www.ygdy8.net].银翼杀手2049.HD.720p.中英双字幕.rmvb',
    '[阳光电影www.ygdy8.net].心理罪之城市之光.HD.720p.国语中字.rmvb',
    '[阳光电影www.ygdy8.net].天才枪手.BD.720p.中文字幕.mkv',
    '[阳光电影www.ygdy8.net].圣鹿之死.HD.720p.中英双字幕.rmvb',
    '[阳光电影www.ygdy8.net].密战.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.net].迷镇凶案.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.net].龙之战.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.net].军舰岛.BD.720p.韩语中字.mkv',
    '[阳光电影www.ygdy8.net].疯狂父母.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].走火交易.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].蜘蛛侠：英雄归来.HD.720p.中英双字幕.rmvb',
    '[阳光电影www.ygdy8.com].战lang2.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.com].银河护卫队2.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].异星觉醒.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].绣春刀II：修罗战场.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.com].星际特工：千星之城.HD.720p.韩版中字.rmvb',
    '[阳光电影www.ygdy8.com].星河战队：火星叛国者.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].新木乃伊.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].心理罪.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.com].嫌疑人X的献身.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.com].王牌保镖.BD.720p.中英双字幕.mkv',
    '[阳光电影www.ygdy8.com].杀破狼·贪狼.HD.720p.国语中字.mkv',
    '[阳光电影www.ygdy8.com].破·局.HD.720p.国语中字.mkv'

]

s1='[阳光电影www.ygdy8.com].变形金刚5：最后的骑士.BD.720p.中英双字幕.mkv'
for file in film_list:
    result = re.match('(\[.+\]\.*)(.+?)(\.*(BD|HD).(.+?))(\.\w{3,4})',file)
    print(result.group(2)+result.group(6))
#filter筛选出[阳光电影www.ygdy8.com]开头的文件，截取文件名中电影名称和后缀，重新生成新文件名。
# list =  map(lambda file:file.split('.')[3]+'.'+file.split('.')[7],filter(lambda file:file[:27]=='[阳光电影www.ygdy8.com]',film_list))
# for file in list:
#     print(file)
