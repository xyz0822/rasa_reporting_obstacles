## intent:greet
- 你好
- 嗨
- 嘿
- 早上好
- 中午好
- 晚上好
- 您好
- hi there
- hello there
- hey
- hi
- hey bot
- good morning
- goodmorning
- hello
- goodevening
- goodafternoon
- good evening
- morning
- good afternoon

## intent:deny
- 否
- 不
- 不 谢谢
- 不用了
- 给的提示都不对
- 不好
- 不同意
- 拒绝
- 不要
- 不想
- 不了
- 不 谢谢 再见
- 没有
- 我不想继续了
- 我不想查了

## intent:bye
- 再见
- 下次见
- 再会
- bye


## intent:query_train
- 查询[掌上生活](train_channel)[火车票](search_channel)
- 查询[掌上生活](train_channel)[火车票](search_channel)订单
- 我想查询[掌上生活](train_channel)[火车票](search_channel)订单[支付状态](train_status)
- 我要查询[掌上生活](train_channel)[火车票](search_channel)订单[退款状态](train_status)
- 查询[掌上生活](train_channel)[火车票](search_channel)[退款状态](train_status)
- 查询[掌上生活](train_channel)[火车票](search_channel)订单[退款状态](train_status)
- [掌上生活](train_channel)[火车票](search_channel)[退款状态](train_status)
- [掌上生活](train_channel)[火车票](search_channel)订单[退款状态](train_status)
- [掌生](train_channel)[火车票](search_channel)[退款状态](train_status)
- [掌生](train_channel)[火车票](search_channel)订单[退款状态](train_status)
- [掌上生活](train_channel)
- [手机银行](train_channel)
- [退款状态](train_status)
- [火车票](search_channel)订单
- 订单号:[12345678111](train_order_id)
- 订单号[12345678111](train_order_id)
- 订单[12345678222](train_order_id)
- [41245634821](train_order_id)
- [52235658821](train_order_id)
- [51245634826](train_order_id)

## regex:train_order_id
- [0-9]{11}


## lookup: train
data/nlu/lookups/train.txt


## intent:out_of_scope
- 你是谁？
- 这个例子主要讲什么
- 实现了什么功能
- 有哪些功能
- 这个例子演示了哪些功能
- 解决了什么问题
- 这是什么？
- 这是啥？
