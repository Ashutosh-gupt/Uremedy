# from neuralintents import GenericAssistant
# import speech
#
# assistant = GenericAssistant('intents.json', model_name="test_model")
# assistant.train_model()
# assistant.save_model()
#
# done = False
#
# while not done:
#     try:
#         message = speech.text
#         if message == "stop":
#             done = True
#         else:
#             assistant.request(message)
#             break
#     except:
#         print("can't recognize anything")
#         break
