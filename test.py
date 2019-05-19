##随机生成字母
# import string,random
# def get_clice(num):
#     res =[]
#     tmp=string.ascii_lowercase #py3 这个函数把大小写都包括进去了
#     for i in range(num):
#         res.append(''.join(random.sample(tmp,4)))
#     return res
# print(get_clice(20))

##字母+数字
# import string,random
# def get_clice(num):
#     res =[]
#     tmp=string.ascii_lowercase #py3 这个函数把大小写都包括进去了
#     tmn=['0','1','2','3','4','5','6','7','8','9']
#     sam=tmp.join(tmn)
#     for i in range(num):
#         res.append(''.join(random.sample(sam,4)))
#     return res
# print(get_clice(20))