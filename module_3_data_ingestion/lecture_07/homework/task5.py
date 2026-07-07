import json
api_response_json = """ 
{ 
	"store": "StoreHub", 
	"orders": [ 
		{"id": 1, "total": 50}, 
		{"id": 2, "total": 200}, 
		{"id": 3, "total": 150} 
		]
 } 
"""

api_response = json.loads(api_response_json)

orders = api_response['orders']

high_value_orders = [i for i in orders if i['total']>100]

api_response['high_value_orders'] = high_value_orders

result = json.dumps(api_response)

print(result)
