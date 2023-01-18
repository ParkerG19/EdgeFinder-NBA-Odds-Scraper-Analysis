from datetime import *



def gettingURL(db, cursor):
    query1 = "SELECT url FROM matchups WHERE date >= %s AND url IS NOT NULL"
    value = str(date.today())
    cursor.execute(query1, (value,))
    result = [ x[0] for x in cursor.fetchall()]

    urlList = []
    for results in result:
        urlList.append(str(results))

    return urlList