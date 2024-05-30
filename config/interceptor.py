from django.shortcuts import redirect
import logging
logger = logging.getLogger(__name__)

def myInterceptor(get_response):

    def middleware(request):
        logger.debug('interceptor!!!')
        # logger.debug('request.path = ', request.path)
        if (
                request.path != '/login/login_page/'
                and request.path != '/login/login_process/'
                and request.path != '/login/logout_process/'
                and request.path != '/login/main_page/'
        ):
            sign_session = request.session.get('sign_session')
            if sign_session is None or sign_session == '':
                return redirect('login/login_page')

        response = get_response(request)
        return response

    return middleware
