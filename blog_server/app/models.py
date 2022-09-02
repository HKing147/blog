from django.db import models

# Create your models here.
# 类别
class Category(models.Model):
    categoryName = models.CharField(max_length=100,verbose_name="类别名",unique=True)
    # users = models.ManyToManyField(to=User)
    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.categoryName
# 标签
class Label(models.Model):
    labelName = models.CharField(max_length=100,verbose_name="标签名",unique=True)
    # users = models.ManyToManyField(to=User)
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.labelName
# 用户
class User(models.Model):
    name = models.CharField(max_length=20,verbose_name="用户名",unique=True)
    password = models.CharField(max_length=20,verbose_name="密码")
    regTime = models.DateTimeField(auto_now_add=True,verbose_name="注册时间")
    avatarPath = models.CharField(max_length=50,default="static/avatars/default.jpeg",verbose_name="头像路径")
    lables = models.ManyToManyField("Label",verbose_name="标签")
    # lables = models.ManyToManyField(to=Label,verbose_name="标签")
    categories = models.ManyToManyField("Category",verbose_name="分类")
    # categories = models.ManyToManyField(to=Category,verbose_name="分类")
    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 文章
class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name="文章标题")
    author = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="作者")
    abstract = models.CharField(max_length=1000,verbose_name="文章摘要")
    category = models.ForeignKey(to=Category,on_delete=models.CASCADE,verbose_name="类别")
    labels = models.ManyToManyField(to=Label,verbose_name="文章标签") # 多个标签用-连接
    content = models.TextField(verbose_name="文章内容")
    coverPath = models.CharField(max_length=50,default="static/covers/default.jpeg",verbose_name="封面路径")
    createTime = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    updateTime = models.DateTimeField(auto_now=True,verbose_name="修改时间")
    views = models.IntegerField(default=0,verbose_name="浏览量")
    likes = models.IntegerField(default=0,verbose_name="点赞数")
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
# 评论
class Comment(models.Model):
    commenter = models.ForeignKey(to=User,on_delete=models.CASCADE,verbose_name="评论者")
    article = models.ForeignKey(to=Article,on_delete=models.CASCADE,verbose_name="评论文章")
    comment = models.TextField(verbose_name="评论内容")
    likes = models.IntegerField(default=0,verbose_name="评论点赞数")
    commentTime = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")
    # author = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="user_id",verbose_name="评论人")
    # article = models.ForeignKey(to=Article,on_delete=models.CASCADE,related_name="article_id",verbose_name="文章")
    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
    def __str__(self):
        self.content