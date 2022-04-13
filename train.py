from neuralintents import GenericAssistant
import speech

import json


def function_for_cold():
    print("1:- Get plenty of fluids. It helps break up your congestion, makes your throat moist, and keeps you away "
          "from "
          "getting dehydrated (water, sports drink, herbal tea)\n2:- take steam")


def function_for_loose_motion():
    print("1:- Hydrating the body is essential to recovering from loose motions\n2:- drink ORS\n3:- Avoid drinking "
          "anything that will further irritate the digestive tract, such as : (caffeinated drinks, alcohol, "
          "carbonated beverages, very hot drinks)")


def function_for_body_pain():
    print("1:- With great antimicrobial and anti-inflammatory properties, apple cider vinegar is definitely a "
          "‘miracle cure’.\n2:- Cinnamon has potent anti-inflammatory, analgesic, and healing properties, "
          "\n    making it one of the most sought-after remedies for treating body pains as well as improving overall "
          "health.\n")


def function_for_headache():
    print("1:- take a pain killer like(crosin) and took a wet towel on your head \n2:- Drink Water. Inadequate "
          "hydration may "
          "lead you to "
          "develop a headache \n3:- Try a B-Complex Vitamin")


def function_for_weakness():
    print("1:- Take steps to control your stress and workload.\n2:- Deal with emotional problems instead of ignoring "
          "or denying them.\n3:- Get enough sleep.\n4:- Eat a balanced diet.\n")


mappings = {'Body Pain': function_for_body_pain, 'headache': function_for_headache, 'Weakness': function_for_weakness,
            'loose motion': function_for_loose_motion, 'cold': function_for_cold}

assistant = GenericAssistant('intents.json', intent_methods=mappings, model_name="test_model")
assistant.train_model()
assistant.save_model()

done = False

while not done:
    try:
        message = speech.text
        if message == "stop":
            done = True
        else:
            assistant.request(message)
            break
    except:
        print("can't recognize anything")
        break
