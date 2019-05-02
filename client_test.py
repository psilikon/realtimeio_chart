import sys
import pprint
import time
from socketIO_client import SocketIO, LoggingNamespace
import MySQLdb
import json

if __name__ == '__main__':
	#db = MySQLdb.connect("192.168.0.250","cron","1234","asterisk")
	db = MySQLdb.connect("127.0.0.1","cron","1234","asterisk",9936)
	cursor = db.cursor()
	
	
	def query_channel_data():
		total_count = 0
		channel_data = []
		# execute SQL query using execute() method.
		sql = """select count(*) AS CHANCOUNT, '192.168.0.251' from live_channels where server_ip = '192.168.0.251'
				UNION
			select count(*) AS CHANCOUNT, '192.168.0.252' from live_channels where server_ip = '192.168.0.252'
				UNION
			select count(*) AS CHANCOUNT, '192.168.0.253' from live_channels where server_ip = '192.168.0.253'
				UNION
			select count(*) AS CHANCOUNT, '192.168.0.254' from live_channels where server_ip = '192.168.0.254'"""

		cursor.execute(sql)
		data = cursor.fetchall()
		for record in data:
			channel_data.append(int(record[0]))
			total_count = total_count + int(record[0])
		
		channel_data.append(total_count)
		return channel_data
	
	

with SocketIO('127.0.0.1', 8000, LoggingNamespace) as socketIO:
    while True:
        # Data for testing
        counts = query_channel_data()
        print counts
        
       
        """
        send_data = {
            counts
        }
"""
        # Send
        socketIO.emit('my event', counts)
     
        time.sleep(5)



