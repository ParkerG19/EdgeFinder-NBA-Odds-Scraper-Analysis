from datetime import *



def gettingURLfd(db, cursor):
    # This query is used to get the fanduel URLS
    query1 = "SELECT fdURL FROM matchups WHERE date >= %s AND fdURL IS NOT NULL"

    value = str(date.today())
    cursor.execute(query1, (value,))
    result = [ x[0] for x in cursor.fetchall()]

    urlList = []
    for results in result:
        urlList.append(str(results))

    return urlList


def gettingURLdk(db, cursor):

    # this query is used to get the URLS for draft kings
    query1 = "SELECT dfURL FROM matchups WHERE date >= %s AND dfURL IS NOT NULL"

    value = str(date.today())
    cursor.execute(query1, (value,))
    result = [ x[0] for x in cursor.fetchall()]

    urlList = []
    for results in result:
        urlList.append(str(results))

    return urlList
