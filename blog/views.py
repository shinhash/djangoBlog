from math import ceil

from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

from blog.utils import dict_sql_post, image_path_rename
import json


def post_create(request):
    if request.method == 'POST':

        if request.FILES:
            my_file = request.FILES['image']
            fs = FileSystemStorage(location='media/images/', base_url='media/images/')

            file_origin_name = my_file.name
            file_trance_name = image_path_rename(my_file.name)
            fs.save(file_trance_name, my_file)

        query_params = {
            'query_id': 'generatePostId',
            'board_id': 'BD001',
        }
        sql = render_to_string('post/model/sql/post.sql', query_params)
        post_id = dict_sql_post(sql)[0].get('POST_ID')

        post_title = request.POST.get('post_title')
        post_cont = request.POST.get('post_cont')

        query_params = {
            'query_id': 'insertPost',
            'board_id': 'BD001',
            'post_id': post_id,
            'post_title': post_title,
            'post_cont': post_cont
        }
        sql = render_to_string('post/model/sql/post.sql', query_params)
        result = dict_sql_post(sql)

        context = {
            'result': 'SUCCESS',
            'post_id': post_id,
        }
        return JsonResponse(context)
    context = {}
    return render(request, 'post/views/post_create.html', context)


def post_list(request):
    page_num = request.POST.get('page_num')
    if page_num is None or page_num == '':
        page_num = 1

    view_cnt = request.POST.get('view_cnt')
    if view_cnt is None or view_cnt == '':
        view_cnt = 5

    page_num = int(page_num)
    view_cnt = int(view_cnt)

    query_params = {
        'query_id': 'selectPostCount',
        'board_id': 'BD001',
    }
    sql = render_to_string('post/model/sql/post.sql', query_params)
    post_cnt = dict_sql_post(sql)[0].get('POST_CNT')

    page_num_limit = (page_num - 1) * view_cnt
    query_params = {
        'query_id': 'selectPostList',
        'board_id': 'BD001',
        'page_num_limit': page_num_limit,
        'view_cnt': view_cnt
    }
    sql = render_to_string('post/model/sql/post.sql', query_params)
    result = dict_sql_post(sql)
    page_len = ceil(post_cnt/view_cnt)

    print('page_num : ', page_num)
    print('view_cnt : ', view_cnt)
    print('page_len = ', page_len)

    context = {
        'post_list': result,
        'page_num': page_num,
        'post_cnt': post_cnt,
        'page_len': page_len,
    }
    return render(request, 'post/views/post_list.html', context)


def post_detail(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        print("detail post_id = ", post_id)
        query_params = {
            'query_id': 'selectPostDetail',
            'board_id': 'BD001',
            'post_id': post_id
        }
        sql = render_to_string('post/model/sql/post.sql', query_params)
        result = dict_sql_post(sql)[0]
        print("result = ", result)
        context = {
            'post': result
        }
        return render(request, 'post/views/post_detail.html', context)
    return redirect('post/list')


def post_update(request):
    context = {}
    return render(request, '', context)


def post_delete(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        post_id = post_data.get('post_id')
        print("post_id info = ", post_id)
        query_params = {
            'query_id': 'deletePost',
            'board_id': 'BD001',
            'post_id': post_id
        }
        sql = render_to_string('post/model/sql/post.sql', query_params)
        result = dict_sql_post(sql)
        context = {
            'result': 'SUCCESS'
        }
        return JsonResponse(context)
    return redirect('post/detail')
