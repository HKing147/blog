import time

from django.db.models import Count, F

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect

from app.models import *
from pprint import pprint
from django.core.files.storage import default_storage
import json


# Create your views here.

def register(request):
    userName = request.GET.get('userName')
    password = request.GET.get('password')
    print(userName,password)
    try:
        res = User.objects.filter(name=userName)
        if len(res) != 0:
            return JsonResponse({"meta": {"status": 400, "msg": "用户已存在！"}})

        User.objects.create(name=userName,password=password)
        return JsonResponse({"meta":{"status":200,"msg":"注册成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta":{"status":400,"msg":"注册失败"}})

def login(request):
    userName = request.GET.get('userName')
    password = request.GET.get('password')
    print(userName,password)

    try:
        user = User.objects.filter(name=userName).first()
        print(user.name,user.password)
        if user.password == password :
            request.session["info"]={"userName":user.name,"userId":user.id}
            return JsonResponse({"data":user.id,"meta":{"status":200,"msg":"登录成功"}})
        else:
            return JsonResponse({"meta":{"status":400,"msg":"登录失败，用户名或密码错误！"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta":{"status":400,"msg":"登录失败，用户名或密码错误！"}})

def logout(request):
    request.session.clear()
    return redirect("/login")

# 获取当前登录用户的相关信息
def getUserInfo(request):
    try:
        userId = request.session.get("info")["userId"]
        print("userId",userId)
        userInfo = [item for item in User.objects.filter(id=userId).values()][0]
        print(userInfo)
        return JsonResponse({"data":userInfo,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

def getCkUserInfo(request):
    try:
        userId = request.GET.get('ckUserId')
        print("userId",userId)
        userInfo = [item for item in User.objects.filter(id=userId).values()][0]
        print(userInfo)
        return JsonResponse({"data":userInfo,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 上传头像
def uploadAvatar(request):
    print("进来了")
    try:
        img = request.FILES['file']
        userId = request.session.get('info')['userId']
        pprint(img)

        timestamp = int(time.time()*1000)
        filepath = 'static/avatars/' + str(userId)+"-"+str(timestamp)+".jpeg"

        with default_storage.open(filepath, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        print(userId)
        print(img.name)
        return JsonResponse({"data":filepath,"meta":{"status":200,"msg":"上传成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "上传失败"}})

# 修改头像路径
def updateAvatar(request):
    try:
        userId = request.session.get('info')['userId']
        avatarPath = request.GET.get('avatarPath')
        print(avatarPath)
        user = User.objects.get(id=userId)
        user.avatarPath = avatarPath
        user.save()
        return JsonResponse({"data":userId,"meta": {"status": 200, "msg": "上传成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "上传失败"}})

# 上传封面
def uploadCover(request):
    print("进来了")
    try:
        img = request.FILES['file']
        userId = request.session.get('info')['userId']
        pprint(img)

        timestamp = int(time.time()*1000)
        coverPath = 'static/covers/' + str(userId)+"-"+str(timestamp) +".jpeg"

        with default_storage.open(coverPath, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        print(userId)
        print(img.name)
        return JsonResponse({"coverPath":coverPath,"meta":{"status":200,"msg":"上传成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "上传失败"}})

# 上传正文图片
def uploadImage(request):
    print("进来了")
    try:
        img = request.FILES['file']
        userId = request.session.get('info')['userId']
        pprint(img)

        timestamp = int(time.time()*1000)
        imagerPath = 'static/images/' + str(userId)+"-"+str(timestamp) +".jpeg"

        with default_storage.open(imagerPath, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        print(userId)
        print(img.name)
        return JsonResponse({"imagerPath":imagerPath,"meta":{"status":200,"msg":"上传成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "上传失败"}})

# 上传评论图片
def uploadCommentImage(request):
    print("进来了")
    try:
        img = request.FILES['file']
        userId = request.session.get('info')['userId']
        pprint(img)

        timestamp = int(time.time()*1000)
        imagerPath = 'static/commentImages/' + str(userId)+"-"+str(timestamp) +".jpeg"

        with default_storage.open(imagerPath, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        print(userId)
        print(img.name)
        return JsonResponse({"imagerPath":imagerPath,"meta":{"status":200,"msg":"上传成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "上传失败"}})

# 写博客
def writeArticle(request):
    try:
        # authorId = request.GET.get('userId')
        authorId = request.session.get('info')['userId']
        title = request.GET.get("title")
        abstract = request.GET.get('abstract')
        categoryId = request.GET.get('categoryId')
        labels = request.GET.get('labels')
        labelsList = labels.split('-')
        print("labelsList",labelsList)
        if labels == '':
            labelsList = []
        coverPath = request.GET.get('coverPath')
        if coverPath == None:
            coverPath = "static/avatars/default.jpeg"
        content = request.GET.get('content')
        print(authorId)
        author = User.objects.filter(id=authorId).first()
        print(title)
        print(abstract)
        print(categoryId)
        print(labels)
        print(coverPath)
        print(content)
        category = Category.objects.get(id=categoryId)
        article = Article.objects.create(title=title,author=author,author_id=authorId,
                               category=category,abstract=abstract,coverPath=coverPath,
                               content=content)

        id = article.id
        # print("==>",article)
        # art = article
        # article.labels.set(*labelsList)
        # article.labels.add(*labelsList)
        print(Article.objects.filter(id=id))
        article = [item for item in Article.objects.filter(id=id).values()][0]
        print(article)
        # art = []
        # print(article.objects.values())
        # art = [item for item in article.objects.values()][0]
        # print(art)
        return JsonResponse({"data":article,"meta": {"status": 200, "msg": "发布成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "发布失败"}})


# 获取类别列表
def getCategoryList(request):
    print("获取类别列表")
    try:
        # categoryList = [model_to_dict(item) for item in Category.objects.all()]
        userId = request.session.get('info')["userId"]
        categoryList = [item for item in User.objects.get(id=userId).categories.all().values()]
        pprint(categoryList)

        return JsonResponse({"data":categoryList,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 获取用户的类别列表（包括每个类别下的文章数）
def getCategoryCount(request):
    try:
        # userId = request.session.get('info')['userId']
        userId = request.GET.get('ckUserId')
        # res = Article.objects.filter(author_id=userId).annotate(count=Count("category_id")).values("count")
        obj = Article.objects.filter(author_id=userId)
        res = obj.values("category_id").annotate(categoryId=F("category_id"),categoryName=F("category__categoryName"),count=Count("category_id")).values("categoryId","categoryName","count")
        categoryCountList = [item for item in res]
        print(categoryCountList)
        return JsonResponse({"data":categoryCountList,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 添加类别
def addCategory(request):
    try:
        userId = request.session.get('info')['userId']
        categoryName = request.GET.get('0')
        category = Category.objects.filter(categoryName=categoryName)
        print("category",category)
        if len(category) == 0:
            category = Category.objects.create(categoryName=categoryName)
        else:
            category = category.first()
        print("category", category)
        User.objects.get(id=userId).categories.add(category)
        return JsonResponse({"meta": {"status": 200, "msg": "添加成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "添加失败"}})

# 添加标签
def addLabel(request):
    try:
        userId = request.session.get('info')['userId']
        labelName = request.GET.get('0')
        label = Label.objects.filter(labelName=labelName)
        print("label",label)
        if len(label) == 0:
            label = Label.objects.create(labelName=labelName)
        else:
            label = label.first()
        print("label", label)
        User.objects.get(id=userId).lables.add(label)
        return JsonResponse({"meta": {"status": 200, "msg": "添加成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "添加失败"}})


# 获取标签列表
def getLabelList(request):
    print("获取标签列表")
    try:
        # labelList = [model_to_dict(item) for item in Label.objects.all()]
        # userId = request.session.get('info')["userId"]
        userId = request.GET.get('ckUserId')
        labelList = [item for item in User.objects.get(id=userId).lables.all().values()]
        pprint(labelList)

        return JsonResponse({"data": labelList, "meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 获取用户的类别列表（包括每个类别下的文章数）
def getLabelCount(request):
    try:
        # userId = request.session.get('info')['userId']
        userId = request.GET.get('ckUserId')
        from django.db.models import Count,F
        # res = Article.objects.filter(author_id=userId).annotate(count=Count("category_id")).values("count")
        # res = obj.values("category_id").annotate(categoryId=F("category_id"),categoryName=F("category__categoryName"),count=Count("category_id")).values("categoryId","categoryName","count")
        # obj = Article.objects.filter(author_id=userId).values()
        # print(obj)
        # for item in obj:
        #     print(item)
        # res = obj.values("labels__labelName")
        # obj.values("labels").annotate(labelId=F("label_id"),labelName=F("label"))
        # res = obj.values("labels").annotate(labelId=F("labels__id"),labelName=F("labels__labelName"),count=Count("id")).values("labelId","labelName","count")
        # print(res)
        # labelList = [labelName for item in User.objects.get(id=userId).lables.values() for labelName in item  ]
        # for item in User.objects.get(id=userId).lables.values("labelName"):
        #     pprint(item)
        #     labels = []
        #     # for label in item:
        #     #     labels.append(label["labelName"])
        #     labelList.append(labels)
        # pprint(labelList)
        articleList = Article.objects.filter(author_id=userId)
        articlelabelList = []
        for item in articleList:
            labels = []
            for label in item.labels.values("labelName"):
                labels.append(label["labelName"])
            articlelabelList.append(labels)
        pprint(articlelabelList)
        labelCountList =[{"labelId":label["id"],"labelName":label["labelName"]} for label in User.objects.get(id=userId).lables.values()]
        # print(labelList)
        print(labelCountList)
        for label in labelCountList:
            count = 0;
            for labels in articlelabelList:
                if label["labelName"] in labels:
                    count += 1
            label["count"]=count
        print(labelCountList)
        return JsonResponse({"data":labelCountList,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 获取文章列表
def getArticleList(request):
    try:
        # userId = request.session.get('info')['userId']
        userId = request.GET.get('ckUserId')
        print(userId)
        print(Article.objects.filter(author_id=userId).values())
        # articleList = [model_to_dict(item) for item in Article.objects.filter(author_id=userId)]
        articleList = [item for item in Article.objects.filter(author_id=userId).values()]

        for item in articleList:
            item['createTime'] = '{:%Y-%m-%d}'.format(item['createTime'])
            item['updateTime'] = '{:%Y-%m-%d}'.format(item['updateTime'])
            # item['createTime'] = '{:%Y-%m-%d %H:%M:%S}'.format(item['createTime'])
            # item['updateTime'] = '{:%Y-%m-%d %H:%M:%S}'.format(item['updateTime'])

        return JsonResponse({"data":articleList, "meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"data": articleList, "meta": {"status": 400, "msg": "获取失败"}})

# 提交评论
def submitComment(request):
    try:
        # commenter = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="评论者")
        # article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name="评论文章")
        # comment = models.TextField(verbose_name="评论内容")
        # likes = models.IntegerField(default=0, verbose_name="评论点赞数")
        # commentTime = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")
        userId = request.session.get('info')["userId"]
        articleId = request.GET.get("articleId")
        content = request.GET.get("content")
        print(userId,articleId,content)
        Comment.objects.create(commenter_id=userId,article_id=articleId,comment=content)
        return JsonResponse({"meta": {"status": 200, "msg": "评论成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "评论失败"}})

# 查询文章的所有评论
def getCommentList(request):
    try:
        articleId = request.GET.get("articleId")
        print(articleId)
        # res = Comment.objects.filter(article_id=articleId).values("commenter__name","commenter__avatarPath")
        # res = Comment.objects.filter(article_id=articleId).annotate(userName=F("commenter__name"),coverPath=F("commenter__avatarPath")).values()
        # print(res)
        commentList = [item for item in Comment.objects.filter(article_id=articleId).annotate(userName=F("commenter__name"),avatarPath=F("commenter__avatarPath")).values()]
        for item in commentList:
            item['commentTime'] = '{:%Y-%m-%d}'.format(item['commentTime'])
            # item['createTime'] = '{:%Y-%m-%d %H:%M:%S}'.format(item['createTime'])
        print(commentList)
        return JsonResponse({"data":commentList,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

def UpdateArticleViews(request):
    try:
        articleId = request.GET.get('articleId')
        article = Article.objects.get(id=articleId)
        article.views += 1
        article.save()
        return JsonResponse({"meta": {"status": 200, "msg": "更新成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "更新失败"}})