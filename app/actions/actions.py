# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import os
import json
import requests
from dotenv import load_dotenv
from rasa_sdk import Action, Tracker
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

load_dotenv()

class ActionCallPokemonAPI(Action):
    
    def name(self) -> Text:
        return "action_call_pokemon_api"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        API_KEY = os.getenv('API_KEY')
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-type": "application/json"}
        link = os.getenv('link')
        id_modelo = os.getenv('id_modelo')

        user_intent = tracker.latest_message['intent'].get('name')
        user_intent = str(user_intent)

        if user_intent == 'pokemon_api':

            user_message = tracker.latest_message['text']
            user_message = str(user_message)

            try:
                body_mensagem = {
                    "model": id_modelo,
                    "messages": [{"role": "user", "content": user_message}] 
                }

                body_mensagem = json.dumps(body_mensagem)

                requisicao = requests.post(link, headers=headers, data=body_mensagem)
                resposta = requisicao.json()
                conteudo = resposta["choices"][0]["message"]["content"]

                dispatcher.utter_message(f"Aqui estão algumas informações sobre Pokémon: {conteudo}")

            except Exception as e:
                dispatcher.utter_message("Desculpe, não consegui encontrar informações.")
                
        return []
        

