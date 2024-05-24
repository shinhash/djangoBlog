
function post_list(page_num){

    let list_form_tag = document.createElement('form');
    list_form_tag.setAttribute('action', $('#list_post_url').val());
    list_form_tag.setAttribute('method', 'post');

    let list_page_tag = document.createElement('input');
    list_page_tag.setAttribute('type', 'hidden');
    list_page_tag.setAttribute('name', 'page_num');
    list_page_tag.setAttribute('value', page_num);

    let list_csrf_token = document.createElement('input');
    list_csrf_token.setAttribute('type', 'hidden');
    list_csrf_token.setAttribute('name', 'csrfmiddlewaretoken');
    list_csrf_token.setAttribute('value', $('#csrf_token').val());

    list_form_tag.appendChild(list_page_tag);
    list_form_tag.appendChild(list_csrf_token);
    document.body.appendChild(list_form_tag);
    list_form_tag.submit();
}




function detail_view(post_id_value){

    let detail_form_tag = document.createElement('form');
    detail_form_tag.setAttribute('action', $('#detail_post_url').val());
    detail_form_tag.setAttribute('method', 'post');

    let detail_post_id = document.createElement('input');
    detail_post_id.setAttribute('type', 'hidden');
    detail_post_id.setAttribute('name', 'post_id');
    detail_post_id.setAttribute('value', post_id_value);

    let detail_csrf_token = document.createElement('input');
    detail_csrf_token.setAttribute('type', 'hidden');
    detail_csrf_token.setAttribute('name', 'csrfmiddlewaretoken');
    detail_csrf_token.setAttribute('value', $('#csrf_token').val());

    detail_form_tag.appendChild(detail_post_id);
    detail_form_tag.appendChild(detail_csrf_token);
    document.body.appendChild(detail_form_tag);
    detail_form_tag.submit();
}


function post_delete(){
    if(!confirm('정말 삭제하시겠습니까?')) return;

    let delete_post_url = $('#delete_post_url').val();
    let post_id = $('#post_id').val();
    let list_post_url = $("#list_post_url").val();
    let csrf_token = $("#csrf_token").val();

    let data_info = {
        'post_id' : post_id
    }
    $.ajax({
        type        : 'POST',
        url         : delete_post_url,
        headers     : {
            "X-CSRFToken" : csrf_token
        },
        data        : JSON.stringify(data_info),
        contentType : false,
        processData : false,
        success     : function (data) {
            if(data.result === 'SUCCESS'){
                alert("삭제 완료");
                window.location.href = list_post_url;
            }else{
                alert("삭제 실패");
            }
        },
        error       : function (error) {
            console.log("error", error);
        }
    });
}


function post_create(){
    let create_post_url = $('#create_post_url').val();
    let form_info = $('#create_post_form')[0];
    let form_data = new FormData(form_info);

    let input_tags = form_info.getElementsByTagName('input');
    for(let i=0; i<input_tags.length; i++){
        let tag_name = input_tags[i].name;
        let tag_value = input_tags[i].value;
        if((tag_name === 'post_title' && tag_value === '')){
            return alert("제목 정보 미입력 됨");
        }
    }

    $.ajax({
        type        : 'POST',
        url         : create_post_url,
        data        : form_data,
        contentType : false,
        processData : false,
        success     : function (data) {
            if(data.result === 'SUCCESS'){
                alert("등록 완료");
                detail_view(data.post_id);
            }else{
                alert("등록 실패");
            }
        },
        error       : function (error) {
            console.log("error", error);
        }
    });
}