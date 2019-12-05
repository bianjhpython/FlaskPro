# FlaskPro
flask 接口开发
<hr>
v1: 接口查询，对sqlalchemy查询的数据进行字典格式序列化
前端使用bootstrap,vue+ajax进行数据渲染，完成页面list_article和articles页面
<br/></br>
v1.1:添加搜索功能，使用title和作者字段进行模糊查询
<br/></br>
v1.2:搜索结合分页功能，使用title和作者字段进行模糊查询，支持搜索后分页保持分页状态
<br/></br>
v1.3:修改post请求，不同功能加载方法


<br/></br>
<br/></br>
<hr>
flask 接口描述

    GET /Api/Article/
    返回 所有文章  
    GET /Api/Article/1/
    返回 id为1的文章
    GET /Api/Article/Search/
        ?search_key=记&page=1
    返回 文章标题和作者含有记的第一页数据
<br/></br>
<br/></br>

附录：
<br/></br>
gs 为古诗词爬虫，用来请求post接口



