# python函数
1.位置参数（必选参数）
def funcname(arg1,arg2,arg3):
    pass
自我理解：所谓位置参数，就是按顺序排列的参数,在调用时，每个位置参数都必须有参数传递
2.默认参数的设置：
def funcname(arg1,arg2_deflut=?):
    //TODO
    return ?
自我理解：默认参数是对位置参数的缺省设置
!!默认参数一定要使用不能更改的对象，如：元组，字符串，数值

3.可变参数的设置：
在位置参数名前加上*
def funcname(*arg):
    //TODO
    return ?

使用：
funcname(1,2,3)
funcname(*list)
funcname(*tuple)

自我理解：通过可变参数位传入的参数在进入函数内部时会被自动钻装成tuple（不可被修改），然后被函数所使用，所以也可以直接通过在list或者tuple对象前加*当做参数传给函数。

4.关键字参数：
def funcname(**kw_arg):
    //TODO
    return ?

使用：
funcname(name='lihua',id=1)
argdit={'name':'lihua','id':1}
funcname(**argdit)
自我理解：可以传入多个关键字参数，以键值对方式传入意味着这些参数将在函数内被组装成dit来使用

5.命名关键字参数(主要用来限制关键字参数的命名和个数)：
用*特殊分隔符来分隔命名关键字参数，可以使用缺省值来简化调用
def funcname(name,*,city,age=18):
    pass
如果已经有了可变参数，在之后的命名关键字参数便可以不用*来分隔
使用：命名关键字参数必须带参数名，不然会报错
funcname('lihua',city='cd',age=18)

参数组合：对于任何一个函数，都能通过func(*agr1,**arg2)的方式调用，不管它的参数和如何定义的

在函数内进行类型检查：用isinstance(x,*datatype)
例如：if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

检查对象是否可迭代：
导入collections模块内的Iterable 
用isinstance()判断

enumerate()可以将list变成索引和值的键值对的可迭代对象

列表生成式：利用range()函数：
list(range(10))
[x for x in range(10)] x可以替换成表达式来生产更加复杂的列表
生成器：g = (x for x in range(10)),在列表生成式外套用()
生成器是个可迭代对象
函数式生产器，在函数定义中，只要包含yield关键字，那么这个函数就不是普通函数，而是一个生成器generator
在迭代函数式生成器的过程中，遇到yield关键字便会中断
匿名函数 lambda arg:func

重要模块：functools :reduce，wraps

callable()变量指向的对象，能否被调用

type()和isinstance()

定制类->实现特殊变量方法:
类的特殊变量：__init__(), __str__(), __len__(), __slots__(), __repr__(),__iter__()，__getitem__(), __setitem__(), __getatrr__()
__call__()
特殊的：常用 __repr__ = __str__

IO:
一般地：open(filename,type,encoding=?,errors='ignore')返回打开文件的引用
type:r读取文本文件（UTF-8）,rb读取二进制文件（图片，视频）,w,wb
对应地:f.read()返回所读到文件内容的str，f.wirte(context),f.close()必须关闭文件，不然会一直占用内存
特别地：with open(filename,type) as f:    会自动地帮我们关闭文件
            //TODO

操作文件和目录：
import os
os.path.abspath('.')显示当前的绝对路径
os.path.join(path,newfile)
os.path.split(path)
os.path.splitext(path)取文件拓展名
os.mkdir('path')
os.rmdir('path')

序列化，不重要的序列化与反序列化方式：pickle.dump(),pikle.load()

重要的序列化方式：JSON（跨语言，通用的标准格式）
通过导入json模块:import json
常用方法:json.dumps(dit),json.dump(dit,file-like-obj)
        json.loads(dit),json.load(dit,file-like-obj)

进程和线程：
进程间通信：通过Queue和Pipes实现的
linux通过fork()调用实现多进程
widows跨平台通过multiprocessing模块实现
线程：
python的线程是真正的Posix Thread，不是模拟出来的线程
多数时候使用threading模块实现线程
启动一个线程就是把一个函数传入线程实例然后调用start()开始执行
t.join()是为了线程同步
Lock->资源锁
例如：
lock = threading.Lock()
def run_thread(n):
    for i in range(10000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


USE database
CREATE database ""
CREATE table table_name(
    id INT,
    name varchar(20),
    sex boolean
);

alter table_name drop clown_nale;
drop table_name;
select * from table_name where 