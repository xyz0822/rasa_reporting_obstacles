import logging
import json
import requests
from rasa_sdk.events import UserUtteranceReverted
from typing import Any, Dict, List, Text, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from discovery import QueryAPI

class QueryTrainRefundForm(FormAction):
    def name(self) -> Text:
        return 'query_train_refund_form'

    @staticmethod
    def required_slots(Tracker):
        return [
            "train_channel",
            "train_order_id",
        ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
             kv={
                 "train_channel":tracker.get_slot("train_channel"),
                 "train_order_id":tracker.get_slot("train_order_id"),
                 "purpose_codes":"ADULT",
                 "leftTicketDTO.from_station":"SHH",
                 "leftTicketDTO.to_station":"BJP",
                 "leftTicketDTO.train_date":"2020-03-20"
                 }
             headers = {"Content-Type": "application/json; charset=utf-8"}
             res = requests.get(url="http://t.weather.sojson.com/api/weather/city/101030100", params=kv, headers=headers)
             dispatcher.utter_message("已获取到信息,业务："+tracker.get_slot("search_channel")+",渠道:"+tracker.get_slot("train_channel")+",订单号:"+tracker.get_slot("train_order_id"))
             dispatcher.utter_message("示例:请求天气查询接口")
             dispatcher.utter_message(res.text)
             return []