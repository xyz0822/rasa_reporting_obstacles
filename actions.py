# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import logging
import json
from typing import Any, Dict, List, Text, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from discovery import QueryAPI

logger = logging.getLogger(__name__)

class TrainForm(FormAction):

    def name(self):
        return "train_form"

    @staticmethod
    def required_slots(Tracker):
        return [
            "train_channel",
            "train_order_id",
        ]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "train_channel":[
                self.from_text(intent="enter_data"),
                self.from_entity(entity="train_channel"),
            ] ,
            "train_order_id":[
                self.from_text(intent="enter_data"),
                self.from_entity(entity="train_order_id"),
            ] 
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
             req = QueryAPI("http://localhost:53345/weatherforecast")
             channel=tracker.get_slot("train_channel")
             order_id=tracker.get_slot("train_order_id")
             req.search("?train_channel="+channel+"&train_order_id="+order_id)
             dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
             return []