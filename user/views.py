from django.shortcuts import render
from django.http import JsonResponse
from .models import CCITUser, AClass, AStudent
import datetime


# Create your views here.

def login(request):
    # render()函数就是用来渲染页面
    return render(request, 'login_js.html')


def userLogin(request):
    result = {'status': 'default', "content": "请求过来了"}
    if request.method == "POST":  # 判断提交的方式
        # 获取参数
        post_data = request.POST
        print(post_data)
        if post_data:
            user = queryUser(post_data)
            if user:
                if user.upwd == post_data['upwd']:
                    result['isUser'] = True
                    result['msg'] = '欢迎登陆'
                    result['user'] = {
                        'uid': user.uID
                    }

                    # 设置会话机制
                    request.session['islogin'] = True

                    # 设置时效 秒
                    request.session.set_expiry(3600)
                else:
                    result['isUser'] = False
                    result['msg'] = '密码错误'
            else:
                result['isUser'] = False
                result['msg'] = '用户名不存在，请联系系统管理员'
    else:
        result['msg'] = '请求Method不正确，请使用POST请求'
        result['content'] = '服务器响应'
    return JsonResponse(result)


def homePage(request, uid):
    print('uid:', uid)

    islogin = request.session.get('islogin')
    if islogin == None:
        return render(request, '404.html', {'msg': u'非法登录!!!!!'})

    # 获取指定用户的班级
    try:
        citems = CCITUser.objects.get(uID=uid).cls.all()
        print(citems)
    except:
        return render(request, '404.html', {'msg': u'该用户下的班级不存在'})

    all_stus = []
    for item in citems:
        try:
            stus = AClass.objects.get(cID=item.cID).stu.all()
            print(stus)
            all_stus.append(stus)
        except:
            return render(request, '404.html', {'msg': u'学生异常，请联系管理员'})

    data = {
        'citems': citems,
        'uid': uid,
        'allstus': all_stus
    }

    return render(request, 'index.html', data)


def queryUser(user):
    try:
        find_user = CCITUser.objects.get(uID=user['uname'])
        return find_user
    except CCITUser.DoesNotExist:  # 异常下的操作，也就是找不到如何处理
        print(u'用户不存在')
    return None


def getAllUser():
    all_users = CCITUser.objects.all()
    datas = []
    if all_users:
        for item in all_users:
            obj = {}
            obj['uID'] = item.uID
            obj['uname'] = item.uname
            obj['uemail'] = item.uemail
            obj['regtime'] = dateToString(item.uregisteredtime)
            obj['ustatus'] = item.ustatus
            datas.append(obj)
        return datas
    else:
        return None


def dateToString(date):
    ds = date.strftime('%Y-%m-%d %H:%M:%S')
    return ds


def stringToDate(string):
    dt = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S+00:00")
    return dt


def querySetsUser(user):
    sets = dict()
    sets['uID'] = user['uname']
    sets['upwd'] = user['upwd']
    find_user = CCITUser.objects.filter(**sets)
    if find_user:
        return find_user
    else:
        return None
