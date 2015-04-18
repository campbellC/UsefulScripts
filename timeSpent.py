import sqlite3 as lite
import time
import calendar
import sys
import re

def chromeTimeToUnixTime(secs):
    return (secs - 11644473600000000) // 1000000 #number of seconds between 1 jan 1601 and 1 jan 1970
def unixTimeToChromeTime(secs):
    return 1000000 * secs + 11644473600000000
def microSecondsToMinutes(msecs):
    return (msecs / 1000000) / 60  


if __name__ == '__main__':
    timeSpan = 24
    if len(sys.argv) != 1:
        timeSpan = sys.argv[1]
    
    currentTime = calendar.timegm(time.gmtime())
    currentTime = unixTimeToChromeTime(currentTime)
    timeSpan = int(timeSpan) * 3600 * 1000000
    startTime = currentTime - timeSpan
    websiteRE = re.compile(r"(?:http://|https://)(?:www\.)?(?P<website>[^.]+\.[^/]+)/.*")
    con = None
    try:
        pass
        con = lite.connect('/Users/chrisCampbell/Library/Application Support/Google/Chrome/Default/History')
    
        cur = con.cursor()
        cur.execute("SELECT urls.url,visit_duration FROM urls, visits WHERE urls.id = visits.url AND visit_time >" + str(startTime) +";")

        rows = cur.fetchall()

        websites = []
        while (len(rows) > 0):
            currentRow = rows.pop(0)
            duration =0 
            match = re.match(websiteRE,currentRow[0])
            if match:
                duration += currentRow[1]
                for row in list(rows):
                    match2 = re.match(websiteRE,row[0])
                    if match2:
                        if match2.group('website') == match.group('website'):
                            duration += row[1]
                            rows.remove(row)
                websites.append([match.group('website'), microSecondsToMinutes(duration)])
        websites.sort(key=lambda x: x[1])
        websites.reverse()
        for i,j in websites:
            if j > 0:
                print i,j
                
        

    finally:
           if con:
               con.close()
