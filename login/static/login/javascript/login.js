function login_process(){
    let form_info = $('#login_form')[0];
    let form_data = new FormData(form_info);

    $.ajax({
        type        : 'POST',
        url         : '/login/login_process/',
        data        : form_data,
        contentType : false,
        processData : false,
        beforeSend  : function(){
            $('#loading-bar').show();
            $('#login_form').hide();
        },
        success     : function (data) {
            if(data.result === 'SUCCESS'){
                alert("로그인 성공");
                window.location.href = '/login/main_page/';
            }else if(data.result === 'FAIL' && data.error_code === 'LOGIN_PW_NE'){
                alert("비밀번호 불일치");
            }
        },
        complete    : function(){
            $('#loading-bar').hide();
            $('#login_form').show();
        },
        error       : function (error) {
            console.log("error", error);
        }
    });
}

function logout_process(){
    let log_out_form = document.createElement('form');
    log_out_form.setAttribute('action', '/login/logout_process/');
    log_out_form.setAttribute('method', 'post');

    let log_out_csrf_token = document.createElement('input');
    log_out_csrf_token.setAttribute('type', 'hidden');
    log_out_csrf_token.setAttribute('name', 'csrfmiddlewaretoken');
    log_out_csrf_token.setAttribute('value', $('#csrf_token').val());

    log_out_form.appendChild(log_out_csrf_token);
    document.body.appendChild(log_out_form);
    log_out_form.submit();
}