{% if query_id == 'selectLoginUser' %}
    SELECT   USER_ID
           , USER_PW
           , USER_NM
           , REG_DT
           , REG_USER_ID
           , REG_IP
           , MOD_DT
           , MOD_USER_ID
           , MOD_IP
           , USE_YN
           , SNS_SIGN_ID
      FROM HASH_SERVER.USERS
     WHERE USE_YN = 'Y'
     {% if login_id %}
       AND USER_ID = '{{ login_id }}'
     {% endif %}
{% endif %}