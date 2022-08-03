import json
from dynamic_compare import get_similarity
from neuralintents import GenericAssistant
import nltk
from functions import get_date_and_time,get_weather,google_search,talk


mappings = {
  "datetime": get_date_and_time,
  "google": google_search,
  "weather": get_weather,
}


nltk.data.path.append("nltk_data")
assistant = GenericAssistant('intents.json',intent_methods=mappings)
assistant.load_model()
with open('intents.json','r') as file:
    intents=json.load(file)



def dynamic_pattern_extracting(message):
    patterns= []
    for intent in intents['intents']:
        for patern in intent['patterns'] :
            similarity = get_similarity(patern, message)
            if (similarity >= 0.9) :
                patterns.append((patern,similarity))
    if len(patterns) > 0 :
        return patterns
    else : return [(message , 0)]

    
def dynamic_chatbot(text):
    patterns= dynamic_pattern_extracting(text)
    if (len(patterns) == 1 and patterns[0][1] == 0 ):
        print(".... ")
        a=assistant.request(patterns[0][0])
    else :
        pattern = get_max_tuple_value(patterns)
        a=assistant.request(pattern[0])
    if a is not None : 
        print(a)
        talk(a)


    

def get_max_tuple_value(patterns):
    max = ('',0)
    for pattern in patterns :
        if pattern[1] > max[1]:
            max = pattern
    return(max)


#dynamic_chatbot("Google russian war")