import pymysql

def connect_mysql(host, port, user, password):
    # 建立数据库连接
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )
    print(conn)
    return conn

def execute_query(conn, query):
    # 创建游标对象
    cursor = conn.cursor()

    # try:
    # 执行查询
    cursor.execute(query)

    # 获取查询结果
    result = cursor.fetchall()
    print(result)
    return result

    # except Exception as e:
    #     print("Error executing query:", e)
    #
    # finally:
        # 关闭游标
    cursor.close()

# 使用示例
conn = connect_mysql('10.64.108.171', 3306, 'cmm-test', 'CDStest.2021')
query = "SELECT * FROM douyin_data.sv_dy_open_access_token where author_id = '93697123755'"
result = execute_query(conn, query)
