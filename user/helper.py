# coding:utf-8
from django.shortcuts import redirect

def login_required(view_func):
    def check(request):
        uid = request.session.get('uid')
        if uid is None:
<<<<<<< HEAD
            return redirect('/user/login')
=======
            return redirect('user/login')
>>>>>>> 343f19cae863de0f7944cd5a59d1de5cc60fa153
        else:
            return view_func(request)
    return check