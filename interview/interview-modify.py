#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# def format(template, data):
#     res = template
#     for dk in data.keys():
#         if dk in template:
#             res = res.replace(dk, str(data[dk]))
#     return res

# str1 = 'name今年age岁了.'
# dit = {
#   'name' : '狮子大哥',
#   'age': 18,
# }
  
# print(format(str1,dit))

dit = {}
str1 = "asdqwdasdqwdasdwq"
for c in str1:
    if c in dit:
        dit[c] += 1
    else:
        dit[c] = 1

res = sorted(dit.items(), key = lambda item: item[0])
print(res)    
    

