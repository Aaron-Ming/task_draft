# coding=utf-8


# 数据库配置

db_config = {
	'host':'101.200.125.9',
	'user':'mingguangzhen',
	'passwd':"123456",
	'db':'cmdb'
}


page_config = {
    "brand_name":'51Reboot',
    'title':'hello reboot',
    "favicon":'https://pic1.zhimg.com/6d660dd4156c64bfad13ff97d79c2f98_l.jpg',
    "menu":[
        {
            # user配置最好不要修改，是和登陆认证相关的，直接在下面加配置即可
            "name": 'user',
            "title": '用户管理',
            "data": [{
                "name": 'username',
                "title": '用户名'
            },{
                "name":'password',
                "title":'密码'
            }]
        },

	{
         "name": 'host',
         "title": '服务器',
         "data": [{
             "name": 'jifang',
             "title": '机房'
         },{
              "name": 'jigui',
             "title": '机柜'
         },{
              "name": 'SN',
             "title": 'SN'
         },{
              "name": 'wanip',
             "title": '公网IP'
         },{
              "name": 'lanip',
             "title": '内网IP'
         },{
              "name": 'iloip',
             "title": '管理IP'
         },{
              "name": 'prog',
             "title": '项目'
         },{
              "name": 'app',
             "title": '应用'
             }]
         }


   ]
     }
