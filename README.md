# Interface_Test
基于python+unittest的简易接口测试框架

使用方法：

一、数据准备： 

1.首先准备测试用例excel； 
	1.1.字段说明： 
		id：用例id 
		名称：随便 
		url：接口url 
		是否执行：yes/no
		请求方式：post/get 
		header(key)：填写请求的header的key，value保存在对应的test_xx.json中
		请求数据（key）：请求数据的key，value保存在对应的test_xx.json中
		依赖用例的id：执行这个请求需要先获取哪个请求的响应信息，就填写这个所需请求的用例id，无论是否执行，都会执行，并且不计入执行用例个数中 
		返回的依赖数据（key）：依赖用例响应信息中，所需目标字段的key 
		依赖数据所处位置：所需目标字段需要替换掉当前所执行请求的字段所处的位置（）
		依赖数据所属字段：依赖请求中，所获取到的依赖数据的字段名，也就是key；比如说：token。则会和上面的数据组成toke:123并随着依赖请求一起发送 
		超时时间：请求获得响应的超时时间设置，单位是秒 
		预期结果：输入本次请求的响应内容中，想要出现的字段（会和实际结果进行in判断） 
		实际结果：执行本次请求后，会把本次的响应信息保存下来（无需填写;ps.相应数据必须为json格式） 
	写完测试用例后，保存在test_data/excel中，并建议取名和test_xx.py文件的名字一样：test_xx.els

2.接着填写data/request/xxx.json（建议取名和对应的test_xx.py文件的名字一样） 这里填写对应的测试用例的请求数据；json格式


3.填写配置文件config/config.ini 
	3.1.字段说明： 
	[server] 和 [content]：邮件的内容配置 
	[path]：报告/日志/测试py文件所在目录等的“项目的相对路径”，不建议修改 
	[test_excel_paht]：测试用例excel的相对路径；可多个（建议取名和对应的test_xx.py文件的名字一样） 
	[test_excel_index]：测试用例excel的sheet的id；可多个（名字和上面对应的一样） 
	[request_json_path]：测试用例对应的请求数据json文件的相对路径；可多个（名字和上面对应的一样） 

二、代码准备 
	1.复制test_case/test_one.py，然后改名成和对应excel一样（方便管理） 
	2.更改文件中的path = ini.get_test_path('test_one')中的test_one，改成和上面的名字一样

三、执行run.py

四、查看结果： 
	1.如果没配置邮箱，则到report/result中去查看html报告和对应的excel文件
	2.如果配置了邮箱，也可以登录收件邮箱进行查看
	
未完成：
	1.数据库相关的，如果有需要的时候再加上去。
	2.添加多线程
