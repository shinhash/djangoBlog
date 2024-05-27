from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from login.utils import dict_sql_login


# Create your views here.
def login_page(request):
    if request.session.get('sign_session'):
        return redirect('login/main_page')
    context = {}
    return render(request, 'login/views/login.html', context)


def login_process(request):
    if request.method == 'POST':

        login_id = request.POST.get('login_id')
        login_pw = request.POST.get('login_pw')

        query_params = {
            'query_id': 'selectLoginUser',
            'login_id': login_id
        }
        sql = render_to_string('login/model/sql/login.sql', query_params)
        print('sql : ', sql)
        user_info_data = dict_sql_login(sql)
        print('user_info : ', user_info)

        login_result = 'FAIL'
        error_code = ''

        if user_info_data is not None and len(user_info_data) > 0:
            user_info_data = user_info_data[0]
            if login_pw == user_info_data.get('USER_PW'):
                login_result = 'SUCCESS'

                request.session['sign_session'] = login_id
                print('sign_user_id : ', request.session.get('sign_session'))
            else:
                error_code = 'LOGIN_PW_NE'

        context = {
            'result': login_result,
            'error_code': error_code,
        }
        return JsonResponse(context)
    return redirect('login/login_page')


def main_page(request):
    context = {}
    return render(request, 'login/views/main.html', context)


def logout_process(request):
    if request.session.get('sign_session'):
        del(request.session['sign_session'])

    context = {}
    return redirect('login/main_page')


def user_info(request):
    context = {}
    return render(request, 'login/views/user_info.html', context)


def sign_up(request):
    context = {}
    return render(request, 'login/views/sign_up.html', context)
