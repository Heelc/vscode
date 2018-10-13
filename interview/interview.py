#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def format(template, data):
    res = template
    for dk in data.keys():
        if dk in template:
            res = res.replace(dk, str(data[dk]))
    return res

str1 = 'name今年age岁了.'
dit = {
  'name' : '狮子大哥',
  'age': 18,
}
  
print(format(str1,dit))

