import time

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
        res = User.objects.filter(name=userName).first()
        print(res.name,res.password)
        if res.password == password :
            request.session["info"]={"userName":res.name,"userId":res.id}
            return JsonResponse({"meta":{"status":200,"msg":"登录成功"}})
        else:
            return JsonResponse({"meta":{"status":400,"msg":"登录失败，用户名或密码错误！"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta":{"status":400,"msg":"登录失败，用户名或密码错误！"}})

def logout(request):
    request.session.clear()
    return redirect("/login")

# 上传图片
def uploadAvatar(request):
    print("进来了")
    try:
        img = request.FILES['file']
        userId = request.session.get('info')['userId']
        pprint(img)

        filepath = 'static/avatars/' + str(userId)+".jpeg"

        with default_storage.open(filepath, 'wb+') as destination:
            for chunk in img.chunks():
                destination.write(chunk)
        print(userId)
        print(img.name)
        return JsonResponse({"meta":{"status":200,"msg":"上传成功"}})
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

# 写博客
def writeArticle(request):
    # authorId = request.GET.get('userId')
    authorId = request.session.get('info')['userId']
    title = request.GET.get("title")
    abstract = request.GET.get('abstract')
    categoryId = request.GET.get('categoryId')
    labels = request.GET.get('labels')
    coverPath = request.GET.get('coverPath')
    content = request.GET.get('content')
    print(authorId)
    author = User.objects.filter(user_id=authorId).first()
    print(title)
    print(abstract)
    print(categoryId)
    print(labels)
    print(content)
    Article.objects.create(title=title,author=author,author_id=authorId,
                           category_id=categoryId,abstract=abstract,
                           labels=labels,coverPath=coverPath,content=content)
    return JsonResponse({"meta": {"status": 200, "msg": "发布成功"}})

# 获取类别列表
def getCategoryList(request):
    print("获取类别列表")
    try:
        # pprint(Category.objects.all())
        # categoryList = [model_to_dict(item) for item in Category.objects.all()]
        categoryList = [item for item in Category.objects.all().values()]
        pprint(categoryList)

        return JsonResponse({"data":categoryList,"meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 添加类别
def addCategory(request):
    try:
        categoryName = request.GET.get('0')
        print(categoryName)
        Category.objects.create(categoryName=categoryName)
        return JsonResponse({"meta": {"status": 200, "msg": "添加成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "添加失败"}})

# 添加标签
def addLabel(request):
    try:
        labelName = request.GET.get('0')
        Label.objects.create(labelName=labelName)
        return JsonResponse({"meta": {"status": 200, "msg": "添加成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "添加失败"}})


# 获取标签列表
def getLabelList(request):
    print("获取标签列表")
    try:
        # labelList = [model_to_dict(item) for item in Label.objects.all()]
        labelList = [item for item in Label.objects.all().values()]
        pprint(labelList)

        return JsonResponse({"data": labelList, "meta": {"status": 200, "msg": "获取成功"}})
    except Exception as e:
        print(e)
        return JsonResponse({"meta": {"status": 400, "msg": "获取失败"}})

# 获取文章列表
def getArticleList(request):
    userId = request.session.get('info')['userId']
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