import logging
import json
import requests
import jieba
import os

from rasa_sdk.events import UserUtteranceReverted
from typing import Any, Dict, List, Text, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from discovery import QueryAPI


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
train_path = f'{project_path}/rasa_reporting_obstacles/data/nlu/lookups/train.txt'
jieba.load_userdict(train_path)

with open(train_path, encoding='utf8') as f:
    STOCK_SET = set(f.read().split('\n'))

class QueryTrainForm(FormAction):
    def name(self) -> Text:
        return 'query_train_form'

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
                 }
             headers = {"Content-Type": "application/json; charset=utf-8"}
             res = requests.get(url="http://t.weather.sojson.com/api/weather/city/101030100", params=kv, headers=headers)
             dispatcher.utter_message("已获取到信息,业务："+tracker.get_slot("search_channel")+",渠道:"+tracker.get_slot("train_channel")+",订单号:"+tracker.get_slot("train_order_id"))
             dispatcher.utter_message("示例:请求天气查询接口")
             dispatcher.utter_message(res.text)
             return []