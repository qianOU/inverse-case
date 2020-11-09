1.在8888端口用charles抓包工具先得到相关的下载url，用正则表达式抽象出来
2.在8080端口用mitmdump启动scrapy.py 抓取匹配的url并进行保存
3.运行douying.py 使手机自动化完成下拉操作


不足：正则表达式写的不够优美
      https://www.cnblogs.com/python-xkj/archive/2018/06/26/9231624.html
      [ ]只能匹配单个字符，用 | 可在多个字符中匹配（2选一） 