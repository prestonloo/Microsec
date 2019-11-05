import asyncio
import websockets
import pymysql
import datetime
from random import randint

async def ws(websocket, path):

    while True:
        
        #comment the 6 lines below to test out with random values between 1 to 100
        #database credentials and execute query to retrieve latest temperature according to time
        db = pymysql.connect("127.0.0.1","root","preston")
        cursor = db.cursor()
        cursor.execute("SELECT `dateTime`,`temperature` FROM microsec.microsec where `dateTime` in (SELECT max(`dateTime`) FROM microsec.microsec)")
        data = cursor.fetchone()
	#format the data and close connection
        now = data[0] + " | " + data[1]
        db.close()
	
        #Uncomment the 4 lines below to test out with random values between 1 to 100
        #today = datetime.datetime.now()
        #now = today.strftime("%d %b %Y %H:%M:%S | ")
        #rand = randint(1, 100)
        #now = now + str(rand)
	
	#send response to client and wait for 10 seconds before querying the database again
        await websocket.send(now)
        await asyncio.sleep(10)

#the websocket serves data at 127.0.0.1 at port 5678
start_server = websockets.serve(ws, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()