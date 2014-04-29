#!/usr/bin/env python
#-*-coding:utf-8-*-

#以只读模式打开文件

f = open('t.txt', 'r')
sum_lines = 0
count_date_item = 0
rt_v_url_count = 0
spec_uid_count = 0
username_list = []
list_date = []
hour_list = []
spec_hour_list = []
source_list = []
rt_content_list = []
rt_num_list = []
uid_list = []
spec_uid_list = []

for line in f:
    sum_lines += 1
    line_list = line.split('",')
    username = line_list[2].strip('\"')
    time = line_list[6].strip('\"')
    date = time.split(' ')[0]
    date_list = date.split('-')
    hour_min_sec = time.split(' ')[1]
    hour = hour_min_sec.split(':')[0]
    source = line_list[7]
    rt_v_url= line_list[-1].strip('\"')
    uid = line_list[1].strip('\"')
    rt_content = line_list[13].strip('\"')
    rt_num = line_list[8].strip('\"')


    username_list.append(username)
    rt_content_list.append(rt_content)
    rt_num_list.append(rt_num)
    uid_list.append(uid)
    list_date.append(date)
    hour_list.append(hour)

    if '2013' == date_list[0] and '11' == date_list[1]:
        count_date_item +=1
    else:
        pass

    if "2013-11-03" == date:
        spec_hour = hour
        spec_hour_list.append(hour)
    else:
        pass

    if source:
        source_list.append(source)
    else:
        pass

    if rt_v_url.startswith("https://twitter.com/umiushi_no_uta"):
        rt_v_url_count += 1
    else:
        pass

    if '573638104' == uid:
        spec_uid_count += 1
    else:
        pass
    
    if '11' == hour:
        spec_uid_list.append(uid)
    else:
        pass
"""
# 1. 首先，统计一下，这个微博的数据一共有多少行.
"""
print '第一题答案是：这个微博一共有：%d行'  % sum_lines
"""
# 2.该微博数据中，一共有多少个不重复的用户名.
"""
#思路：利用集合去重，然后用len取长度
print '第二题答案是：不重复的用户名有：%d个' % len(set(username_list))
"""
# 3.依次输出上面这些，用户名.
""" 
print "第三题答案是：" 
for username in set(username_list):
    print username,
print '\n'
"""
# 4.该微博数据中，有多少条是在2013年11月发布的.
"""
#思路：截取等于2013并且等于11月的
print '第四题答案是：在2013年11月总共发布：%d' % count_date_item
"""
# 5.该微博数据中，有哪些天的数据？（要求：排好序输出为一个list，例：['2013-03-04','2013-03-05'])
""" 
list_set_date = list(set(list_date))
list_set_date.sort()
print '第五题答案是：',list_set_date
"""
# 6.一共有多少天的数据?
"""
print "第六题答案是：一共有%d天的数据" % len(list_set_date)
"""
# 7.该微博数据中，每个小时的发布量各是多少？(提示利用好字典类型)
"""
#思路：利用字典建立一个字典计数器，根据键值的唯一性，输入有重复值的列表，然后利用字典的get方法计数
hour_counter = {}
for item in hour_list:
    hour_counter[item] = hour_counter.get(item, 0) + 1
hour_distribute = [(h, freq) for h, freq in hour_counter.items()]
print "第七题答案是：该微博数据中，每个小时的发布量各是:\n" , hour_distribute
"""
# 8.该微博数据中，哪个小时的发布量最大？(可选题 ，需要lambda来排序)
"""
sorted_hour_distribute = sorted(hour_counter.items(), key = lambda hour_counter:hour_counter[1])

print "第八题答案是：最大发布量:\n",sorted_hour_distribute[-1]
"""
# 9.请按照时间顺序输出 2013-11-03 每个小时的发布微博的频率,
返回结果：[('00', 197), ('01', 184), ('02', 185), ('03', 220)] 等，
要按顺序排好 :)
"""
spec_hour_counter = {}

for item in spec_hour_list:
    spec_hour_counter[item] = spec_hour_counter.get(item, 0) + 1
spec_hour_distribute = [(sh, freq) for sh, freq in hour_counter.items()]
sorted_spechour_distribute = sorted(spec_hour_counter.items(), key = lambda spec_hour_counter:spec_hour_counter[0])
print "第九题答案是：每个小时发布微薄的频率为：\n",sorted_spechour_distribute

"""
# 10. 统计这些数据里面，发布来源都是哪里的，并且输出他们各自的发布次数.
"""
#1. 一共有多少个来源？
list_set_source = list(set(source_list))
print "第十题第一问答案是：一共有多少来源：\n",len(list_set_source)

#2. 每个来源的发布次数，各是多少？

s_counter = {}

for item in source_list:
    s_counter[item] = s_counter.get(item, 0) + 1
s_distribute =  [(s, freq) for s, freq in s_counter.items()]
print "第十题第二问答案是：每个来源的发布次数为：\n",s_distribute
#3. 发布量最大的两个来源是用的什么设备？ (可选题，提示：会用到lambda来排序)
sorted_s_distribute = sorted(s_counter.items(), key = lambda s_counter:s_counter[1])
print "第十题第三问答案是：\n",sorted_s_distribute[-1], sorted_s_distribute[-2]

"""
# 11.计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有多少个?
"""
#思路：以特定url开头的计数一次
print  "第十一题答案是：\n",rt_v_url_count


"""
# 12.UID为573638104的用户 发了多少个微博.
"""
#思路：等于uid计数一次
print "第十二题答案是：\n",spec_uid_count

"""
# 13.该微博数据中，谁发的单条微博内容字数最多，输出这个用户的 用户名.
"""
#思路： 新建一个已经按长度排好的列表，去出最大值，在原列表找出对应下标，然后利用下标在对应username中输出结果
new_rt_content_list = sorted(rt_content_list, key = lambda x:len(x))
max_content_index = rt_content_list.index(new_rt_content_list[-1])
print "第十三题答案是：",username_list[max_content_index]

"""
# 14.该微博数据中，谁转发的数量最多,输出用户的uid.
"""
#思路：利用列表的对应性，即转发量列表中最大值，和对应的uid列表应该是一一对应的
max_rt_num_index = rt_num_list.index(max(rt_num_list))

print "第十四题答案是：",uid_list[max_rt_num_index]

"""
15.该文本里，11点钟，谁发的微博次数最多.
（要求：输出用户的uid，发微博最多次数同时有多人情况下，输出其中一位即可，主要看你的思路和方法）
"""

#思路：统计11点中uid对应发微薄的频率，然后利用max方法直接找大频率对应的uid
spec_uid_counter = {}

for item in spec_uid_list:
    spec_uid_counter[item] = spec_uid_counter.get(item, 0) + 1
    
one_uid = max(spec_uid_counter, key = lambda spec_uid_counter:spec_uid_counter[1])

print "第十五题答案是：",one_uid

f.close()