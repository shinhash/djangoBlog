from datetime import datetime
from uuid import uuid4
from django.db import connections


def dict_sql_login(sql, using='mariaDB'):
    with connections[using].cursor() as cursor:
        cursor.execute(sql)
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]


def image_path_rename(filename):
    ext = filename.split('.')[-1]
    now = datetime.now()
    this_time = now.strftime('%Y%m%d%H%M%S')
    time_uuid = this_time + '_' + uuid4().hex
    file_trance_name = '{}.{}'.format(time_uuid, ext)
    return file_trance_name


def dict_fetchall(sql, using='mariaDB'):
    with connections[using].cursor() as cursor:
        cursor.execute(sql)
        desc = cursor.description
        dict_list = []
        for row in cursor.fetchall():
            zip_result = zip([col[0] for col in desc], row)
            dict_list.append(dict(zip_result))

        return dict_list
