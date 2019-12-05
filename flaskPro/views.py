from app import app,api
from flask import render_template
from flask_restful import Resource
from flask import request

@app.route("/index/")
def setPage():
	return render_template("index.html")

@app.route("/add_page/")
def add_page():
	return render_template("add_article.html")

@app.route("/list_page/")
def list_page():
	return render_template("list_article.html")

@app.route("/article/<int:id>/")
def article(id):
	return render_template("articles.html",aritcle_id = id)

import datetime
from models import Article

class ArticleResource(Resource):
	def __init__(self):
		super(ArticleResource,self).__init__()
		self.response = {
			"version": "v1.0",
			"code": 200,
			"data": [

			]
		}

	def get_dict(self,data):
		obj_dict = data.__dict__
		obj_dict.pop("_sa_instance_state")
		obj_dict["public_time"] = obj_dict["public_time"].strftime("%Y-%m-%d %H:%M:%H")
		return obj_dict

	def get(self,**keywords):
		history_url = request.url
		article_id = keywords.get("article_id")
		if article_id:
			article = Article.query.get(int(article_id))
			dict_data = self.get_dict(article)
			self.response["data"].append(dict_data)
		else:
			if keywords["doing"] == "Search":
				search_key = request.args.get("search_key")
				page = int(request.args.get("page",1))
				page_size = 20
				articles = Article.query.paginate(page,page_size)
				article_list = [self.get_dict(art) for art in articles.items]
				self.response["page"] = list(range(1,articles.pages+1))
				self.response["data"] = article_list
			else:
				articles = Article.query.all()
				article_list = [self.get_dict(art) for art in articles]
				self.response["data"] = article_list
		self.response["history_url"] = history_url
		return self.response

	def post(self):
		if request.method == "POST":
			title = request.form.get("title")
			author = request.form.get("author")
			description = request.form.get("description")
			content = request.form.get("content")
			public_time = request.form.get("p_time")

			article = Article()
			article.title = title
			article.author = author
			article.description = description
			article.content = content
			if public_time:
				article.public_time = public_time
			else:
				article.public_time = datetime.datetime.now()
			article.save()

			self.response["data"].append("")

		return self.response

	def put(self):
		return "put"

	def delete(self):
		return "delete"



#POST "/Api/Article/search/" {"ordering": "","desc": True, "key" : "", "include_field": []}

api.add_resource(ArticleResource,
				 "/Api/Article/",
				 "/Api/Article/<int:article_id>/",
				 "/Api/Article/<string:doing>/"
				 )

#加入token验证
	#请求token
	#下发token
	#使用token
	#校验token
