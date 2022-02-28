while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastAPI', user='postgres', password='anjana99', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('DB connection was successful')
        break
    except Exception as error:
        print('connecting to DB failure')
        print("Error: " + error)
        time.sleep(2)
