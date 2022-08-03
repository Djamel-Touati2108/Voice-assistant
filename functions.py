from datetime import date ,datetime
import urllib.request
import locationtagger
import nltk
import json
import requests
import pyttsx3 as tts

nltk.data.path.append("nltk_data")

speaker = tts.init()
speaker.setProperty('rate', 120)


def talk(text):
    speaker.say(text)
    speaker.runAndWait()   
    
def get_date_and_time(x):
    time = datetime.now()
    today = date.today()
    d = today.strftime("%B %d, %Y")
    dt_string = time.strftime("%H:%M")
    t=("Today's date is : "+ d +" and time is "+dt_string )
    print(t)
    talk(t)
    


def get_city_from_ip():
    
    url = 'http://ipinfo.io/json'
    response = urllib.request.urlopen(url)
    data = json.load(response)
    city = data['city']
    return(city)
  


def get_city_from_string(s):
    place_entity = locationtagger.find_locations(text = s)
    return(place_entity.cities)


def get_weather(text):

    city = get_city_from_string(text)

    if len(city) == 0:
        city = get_city_from_ip()
    else : city = city[0]
    
    api_key = "get your personal key "
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api_key)
    response = requests.get(url)
    x = response.json()
    if x['cod'] != 404 :

        t=("the weather in "+x['name']+' is '+x['weather'][0]['main']+ ' with '+x['weather'][0]['description'])
    else : t= ('An error occured while getting the weather')
    print(t)
    talk(t)


def google_search(query):
    

    base_url = "https://google-search3.p.rapidapi.com/api/v1/search/q="

    headers = {
        "X-User-Agent": "desktop",
        "X-Proxy-Location": "EU",
        "X-RapidAPI-Key": "get your personal key ",
        "X-RapidAPI-Host": "google-search3.p.rapidapi.com"
    }
    query=query.lower()
    query=query.replace('google ','')
    query=query.replace('search ','')
    query=query.replace(' ','+')
    url=base_url+query
    response = requests.request("GET", url, headers=headers)
    results=response.json()
    final_results = beutify_response(results)
    i=1
    for r in final_results.items() :
        n='result number '+str(i)
        talk(n)
        print(r[1]['title'])
        talk(r[1]['title'])
        i=i+1


def beutify_response(json_rsponse):
    i=0
    responses={}
    for response in json_rsponse['results']:
        if i<5:
            key='response'+str(i)
            responses[key]={'title':response['title']}
            i=i+1
    return(responses)     




       
