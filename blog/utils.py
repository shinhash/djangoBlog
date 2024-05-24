from datetime import datetime
from uuid import uuid4
from django.db import connections


def dict_sql_post(sql, using='default'):
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
