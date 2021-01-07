import requests
import get_cred

key =  get_cred.return_power_api_key() 

def running_avg(new_val, my_lat=35.45, my_long=-82.98):
    avg_power_rates = requests.get('https://developer.nrel.gov/api/utility_rates/v3.json?api_key=' + key + '&lat=' + str(my_lat) +'&lon=' + str(my_long) +'')
    print(avg_power_rates.text)

running_avg(None)

