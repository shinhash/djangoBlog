{% if query_id == 'selectPostList' %}
    SELECT   BOARD_ID
           , POST_ID
           , POST_TITLE
           , POST_CONT
           , REG_DT
           , REG_USER_ID
           , REG_IP
           , MOD_DT
           , MOD_USER_ID
           , MOD_IP
           , USE_YN
      FROM DJANGO_MARIADB.POST
     WHERE 1 = 1
       AND USE_YN = 'Y'
    {% if board_id %}
       AND BOARD_ID = '{{ board_id }}'
    {% endif %}
        ORDER BY REG_DT DESC
    LIMIT {{ page_num_limit }}, {{ view_cnt }}
{% endif %}


{% if query_id == 'selectPostDetail' %}
    SELECT   BOARD_ID
           , POST_ID
           , POST_TITLE
           , POST_CONT
           , REG_DT
           , REG_USER_ID
           , REG_IP
           , MOD_DT
           , MOD_USER_ID
           , MOD_IP
           , USE_YN
      FROM DJANGO_MARIADB.POST
     WHERE 1 = 1
    {% if board_id %}
        AND BOARD_ID = '{{ board_id }}'
    {% endif %}
    {% if post_id %}
        AND POST_ID = '{{ post_id }}'
    {% endif %}
{% endif %}


{% if query_id == 'deletePost' %}
    UPDATE DJANGO_MARIADB.POST
       SET USE_YN = 'N'
     WHERE POST_ID = '{{ post_id }}'
{% endif %}


{% if query_id == 'selectPostCount' %}
    SELECT COUNT(1) as POST_CNT
      FROM DJANGO_MARIADB.POST
     WHERE 1 = 1
       AND USE_YN = 'Y'
    {% if board_id %}
       AND BOARD_ID = '{{ board_id }}'
    {% endif %}
{% endif %}


{% if query_id == 'generatePostId' %}
    SELECT    CASE WHEN MAX(POST_ID) IS NOT NULL
                   THEN CONCAT('P', DATE_FORMAT(SYSDATE(), '%Y%m%d%H%i'), '_', (LPAD((SUBSTR(MAX(POST_ID), 15, 3) + 1), 3, '0')) )
                   ELSE CONCAT('P', DATE_FORMAT(SYSDATE(), '%Y%m%d%H%i'), '_001')
                   END AS POST_ID
      FROM DJANGO_MARIADB.POST
     WHERE 1 = 1
       AND BOARD_ID = '{{ board_id }}'
       AND DATE_FORMAT(SYSDATE(), '%Y%m%d%H%i') = SUBSTR(POST_ID,2,12)
{% endif %}


{% if query_id == 'insertPost' %}
     INSERT INTO DJANGO_MARIADB.POST(
                      BOARD_ID
                    , POST_ID
                    , POST_TITLE
                    , POST_CONT
                    , REG_DT
                    , REG_USER_ID
                    , REG_IP
                    , MOD_DT
                    , MOD_USER_ID
                    , MOD_IP
                    , USE_YN
                ) VALUES(
                    '{{ board_id }}'
                  , '{{ post_id }}'
                  , '{{ post_title }}'
                  , '{{ post_cont }}'
                  , DATE_FORMAT(SYSDATE(), '%Y%m%d%H%i%s')
                  , 'admin'
                  , '127.0.0.1'
                  , DATE_FORMAT(SYSDATE(), '%Y%m%d%H%i%s')
                  , 'admin'
                  , '127.0.0.1'
                  , 'Y'
                )
{% endif %}