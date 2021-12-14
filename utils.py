import requests
import json
import os 

folder_name =os.path.dirname(os.path.abspath(__file__))

base_url = "https://adventofcode.com/2021/day/{}/input"

session_cookie_id = "53616c7465645f5fdcb56ef5be8d1b41167b516cdf0c71ebbe8c4bcb7718dcd869f6929acc2f1c0e05761981ff73ab34"

def cache(function):
    file = open(folder_name + "/cache.dat" , "r")
    data = json.loads(file.read())
    file.close

    def decorator(day):
        if day not in data:
            input = function(day)
            data[day] = input
            file = open(folder_name + "/cache.dat"   , "w")
            file.write(json.dumps(data))
            file.close()

        return data[day]
    return decorator

@cache
def get_input(day):
    url = base_url.format(day)
    cookies = {
        "session": session_cookie_id
    }
    r = requests.get(url , cookies=cookies)
    return r.text

day_1 = get_input(day=1)
