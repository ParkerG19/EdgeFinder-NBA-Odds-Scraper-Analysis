from datetime import *


"""
This function will take in a database connection and the corresponding cursor
and query the database for URL's that will be currently available on fanduel

A URL is considered available if it not NULL and the date is the current date
or later. This way it would not get anything for games in the past
"""

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

"""
This function will take in a database connection and the corresponding cursor
and query the database for URL's that will be currently available on draftKings

A URL is considered available if it not NULL and the date is the current date
or later. This way it would not get anything for games in the past
"""

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

