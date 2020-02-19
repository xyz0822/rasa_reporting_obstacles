# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import logging
import json
import requests
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
             kv={"train_channel":tracker.get_slot("train_channel"),"train_order_id":tracker.get_slot("train_order_id")}
             headers = {"Content-Type": "application/json; charset=utf-8"}
             res = requests.get(url="http://www.baidu.com", params=kv, headers=headers)
             dispatcher.utter_message("准备信息完毕")
             dispatcher.utter_message("Ok,请求url:www.baidu.com,返回的值:"+res.text)
             return []
