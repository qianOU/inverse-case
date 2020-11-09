1.Chormedriver是与Chrome v75.0.3770.100版本相匹配的

2.必须将Chromedriver拖动到Python目录下的Scripts文件夹下

3.需要安装selenium库,可以使用pip命令在终端进行下载

4.直接运行run.py就会自动更新学术报告与新闻速递

5.settings.py是保存部分配置信息，用户名与密码

6.documents文件夹保存的是从理学院爬下来的有关数学的文件

7.SPEECHES文件夹集成了有关学术报告的所有程序,主要便于调试

8.NEWS文件夹集成了有关新闻的所有程序,主要便于调试

9.注：可直接运行run.py即可

10.对于配置信息的更改可直接更改与run.py同级的settings

11.由于用自动化selenium控制Chrome浏览器，有时会不稳定导致程序异常。此时只要重新运行run.py即可。因为
   这里的检测更新是实时与理学院官网进行比较的。确保了不会重复，不遗漏。