# Generated by Django 4.1 on 2022-09-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('abstract', models.CharField(max_length=1000, verbose_name='文章摘要')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('coverPath', models.CharField(default='static/covers/default.jpeg', max_length=50, verbose_name='封面路径')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.IntegerField(default=0, verbose_name='点赞数')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100, unique=True, verbose_name='类别名')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelName', models.CharField(max_length=100, unique=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('regTime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('avatarPath', models.CharField(default='static/avatars/default.jpeg', max_length=50, verbose_name='头像路径')),
                ('categories', models.ManyToManyField(to='app.category', verbose_name='分类')),
                ('lables', models.ManyToManyField(to='app.label', verbose_name='标签')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='评论内容')),
                ('likes', models.IntegerField(default=0, verbose_name='评论点赞数')),
                ('commentTime', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.article', verbose_name='评论文章')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='评论者')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='类别'),
        ),
        migrations.AddField(
            model_name='article',
            name='labels',
            field=models.ManyToManyField(to='app.label', verbose_name='文章标签'),
        ),
    ]
