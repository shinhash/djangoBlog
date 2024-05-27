from django.shortcuts import redirect


def myInterceptor(get_response):

    def middleware(request):
        print('interceptor!!!')
        print('request.path = ', request.path)
        if request.path == '/login/login_page/' or request.path == '/login/login_process/':
            print("login")
        else:
            sign_session = request.session.get('sign_session')
            print('sign_session : ', sign_session)
            if sign_session is None or sign_session == '':
                return redirect('login/login_page')

        response = get_response(request)
        return response

    return middleware
