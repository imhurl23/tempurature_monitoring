# Izzy Hurley and Luis Baez
# CS431 Project 
# Functions to read from the database



from pprint import pprint
import boto3
from botocore.exceptions import ClientError
import json
from decimal import Decimal
import datetime

#not currently used but left in case we wanted to use it later
class DecimalEncoder(json.JSONEncoder):
	def default(self,obj):
		if isinstance(obj, Decimal):
			return str(obj)
		return json.JSONEncoder.default(self,obj)\

#not currently used but left in case we wanted to use it later
def round_minutes(dt, direction, resolution):
    new_minute = (dt.minute // resolution + (1 if direction == 'up' else 0)) * resolution
    return dt + datetime.timedelta(minutes=new_minute - dt.minute)

#not currently used but left in case we wanted to use it later
def get_tval(offset):
    dt = datetime.datetime.now()
    val = round_minutes(dt,'down',5)
    #print(val)
    final_time = val + datetime.timedelta(minutes=offset)
    
    # print("FINAL TIME:"+final_time)
    if final_time>dt:
        final_time = final_time + datetime.timedelta(minutes=-5)
    final_time = final_time + datetime.timedelta(hours= -5)
    final_time = final_time.strftime('%H:%M:%S')
    final_time = final_time[0:-3]
    
    print ('rounded',final_time)
    return final_time


# get the temperature at a given timestamp
def get_temps(timestamp, dynamodb=None):
    #timestamp = get_tval(3)
    if not dynamodb:
            dynamodb =  boto3.resource('dynamodb',region_name = 'us-west-2')
    table = dynamodb.Table('test_t')
    try:
        response = table.get_item(Key = {'timestamp':timestamp})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        jsonString = json.dumps(response['Item'],cls = DecimalEncoder)
        jsonFile = open('temps.json','w')
        jsonFile.write(jsonString)
        jsonFile.close()
        return response['Item']
                #else:
                   # print({'device_1': -9999, 'day': '00/00/00', 'device_2': -9999, 'timestamp': '99:99'})


#get all the temperature readings from the database
def get_ALL_temps(dynamodb=None):
    #timestamp = get_tval(3)
    if not dynamodb:
            dynamodb =  boto3.resource('dynamodb',region_name = 'us-west-2')
    table = dynamodb.Table('test_t')
    try:
        response = table.scan()
        print(response)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']






if __name__ =='__main__':
    temp_resp = get_temps()
    print('get temp succeeded')
    pprint(temp_resp,sort_dicts = False)
    get_tval(2)
