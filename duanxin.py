import socket
import datetime
import threading
print('''
                   , - ~ ~ ~~ -,  /' ' ` ` ' ` ~ -, 
	                  /     , . . - ~' /   /' ~ - . , . -' 
	                 '|     |          /   / 
	                  \    '|  ¸ -' ,''-' ,'-,           , - ~ , 
	                    \   \' ( ,'      ', '-,     ¸.-( ¸ ¸ #,' 
	                    （\''-，，º,,''º-''（'（'， 
	                     '-,        ¸ ¸                      , ' 
	                        '-,    '  ;  - . , , , ,  .  - ' 
	                            '\'-,   ', '\;' ~,  ' , 
	                              \,'-¸¸ '-¸¸'\,   '   ', 
	                           -:' ¸ , . , , , ,`,';' ' 
	                           ,-',               ' , 
	            ,.,           ,'-'                   ', 
	         ,-'     '-,    ,-'       /,.-            ,' 
	        ;          ',,-'      ,-'               ,-', ¸ 
	        ',     \`    \      -'               ,-'     ,' 
	         ',     \     ',     \          , -'   '-  ,-' 
	          ;      \     ',     \   - ~,' \      ', 
	          ,'~    ',     ;      ',,.-','    ',     ', 
	       , '         ', , , ;      ', ,'    /¸|    --', ¸ 
	      (¸¸¸)¸¸¸¸)¸¸¸)    ,'         ' ,   ,'         '-,) 
	        Ñë§§       (¸¸¸¸)¸¸¸¸)¸¸¸¸)(¸¸¸¸)¸¸¸¸)¸¸¸¸)«

Welcome !!!
It's useful for you!!!
''')
print('''
选择模式：
1，查询本机ip（内网）
2.娱乐，打印乘法表
3，查询本地计算机名
4，查询当前时间
5，查询当前星期
''')
a=input('输入选择:')
a=int(a)
myname=socket.getfqdn(socket.gethostname())
def ip1():
    global a
    global myname
    if a==1:
        my_ip=socket.gethostbyname(myname)
        print('你的ip地址是:',my_ip)
    else:
        pass
    return None;
def name():
    global a
    global myname
    if a==3:
        print('你的计算机名为:',myname)
    else:
        pass
    return None;
def time():
    global a
    if a==4:
        b=datetime.datetime.now()
        print('现在时间是:',b)
    else:
        pass
    return None;
def ip_a():
    global a
    if a==2:
        print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
    else:
        pass
    return None;
def xingqi():
    global a
    if a==5:
        clj=datetime.datetime.now().strftime('%A')
        clj=str(clj)
        print(clj)
    else:
        pass
    return None;
#主函数
def main():
    start=threading.Thread(target=xingqi,args=())
    start1=threading.Thread(target=ip_a,args=())
    start2=threading.Thread(target=time,args=())
    start3=threading.Thread(target=name,args=())
    start4=threading.Thread(target=ip1,args=())
    start.start()
    start1.start()
    start2.start()
    start3.start()
    start4.start()
if __name__ == '__main__':
    main()





