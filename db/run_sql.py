import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    results = []
    conn = None

    try:
        conn=psycopg2.connect("dbname='hutchVets'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
