from django.db import models


# Create your models here.
class CCITUser(models.Model):
    # id = models.AutoField(primary_key=True)
    uID = models.CharField('用户ID', max_length=11, unique=True)
    upwd = models.CharField('密码', max_length=18)
    uname = models.CharField('姓名', max_length=128)
    uregistertime = models.DateTimeField('注册时间', auto_now_add=True)
    uemail = models.CharField('邮箱', max_length=128)
    ustatus = models.CharField('用户状态', max_length=1)

    class Meta:
        verbose_name_plural = '班级管理员s'
        verbose_name = '班级管理员'
        db_table = 'class_table'
        ordering = ['uID']

    def __str__(self):
        return self.uID


class AClass(models.Model):
    cID = models.CharField('班级ID', max_length=11, unique=True)
    cn = models.CharField('班级名称', max_length=128)
    cETD = models.CharField('学院/系名称', max_length=128)
    cadmin = models.ForeignKey('CCITUser', null=False, related_name='cls', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '班级管理'
        verbose_name = '班级'
        db_table = "classes_table"
        ordering = ['cID']  # 排序

    def __str__(self):
        return self.cn

# 构建学生数据模型
class AStudent(models.Model):
    sID = models.CharField('学号', max_length=11, unique=True)
    sname = models.CharField('姓名', max_length=128)
    stel = models.CharField('手机号', max_length=11, unique=True)
    sage = models.CharField('年龄', max_length=3)
    ssex = models.CharField('性别', max_length=1)
    smajor = models.CharField('专业', max_length=128)

    # 外链
    aclass = models.ForeignKey('AClass', null=False, related_name='stu', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '学生管理s'
        verbose_name = '学生'
        ordering = ['sID']

    def __str__(self):
        return '%s:%s' % (self.sID, self.sname)
