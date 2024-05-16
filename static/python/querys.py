login_query = """
    SELECT * FROM user
    WHERE id = %s and password = %s
"""

check_id_query = """
    SELECT * FROM user
    WHERE id = %s
"""

signup_query = """
    INSERT INTO user
    VALUES(%s, %s, %s)
"""