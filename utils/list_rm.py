#!/usr/bin/env python3

from sub_convert import sub_convert   # Python 之间互相调用文件https://blog.csdn.net/winycg/article/details/78512300
import json, re
import sys, getopt
from urllib import request

# 文件路径定义
def main(argv):
   input_file = ''
   output_file = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["input=","output="])
   except getopt.GetoptError:
      print ('test.py -i <input_file> -o <output_file>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'with -i <input_file> -o <output_file>'
         sys.exit()
      elif opt in ("-i", "--input"):
         input_file = arg
      elif opt in ("-o", "--output"):
         output_file = arg
   print ('input_file')
   print ('output_file')

file_list = []  #创建一个空列表

class sub_merge:
    def out_file(): #文件去重
        #file_2 = open_file()   #打开需要去重的文件
        with open(input_file, 'r', encoding='utf-8') as f:
            while True:
                url=f.readline()
                if url:
                    file_list.append(url)
                else:
                    break
            #last_out_file=list(set(file_list)) #set()函数可以自动过滤掉重复元素   但是不保证原顺序
            last_out_file=list(dict.fromkeys(file_list)) #python3.6之后 dict()函数可以自动过滤掉重复元素，保证原顺序
            n=len(last_out_file)
            l=len(last_out_file)
            with open(output_file,'w',encoding='utf-8') as f:   #去重后文件写入文件里
                f.seek(0)
                f.truncate()   #清空文件
                #print(file_list[0])
                while n:
                    f.write(file_list[0]+"\n")
                    #f.write(file_list[0])
                    n=n-1
                    del file_list[0]
            print(l)

if __name__ =="__main__":
    sub_merge.out_file()
    main(sys.argv[1:])
