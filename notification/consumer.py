from redis_om import get_redis_connection
import time

redis = get_redis_connection(
    host="redis",
    port=6379,
    decode_responses=True
)

streams = ["order_completed", "refund_order"]
group = "notification-group"

for stream in streams:
    try:
        redis.xgroup_create(stream, group, mkstream=True)
    except:
        print(f"Group already exists for {stream}")

while True:
    try:
        results = redis.xreadgroup(
            group,
            "notification-consumer",
            {stream: '>' for stream in streams},
            count=1,
            block=5000
        )

        if results:
            for result in results:
                stream_name = result[0]
                message = result[1][0][1]

                if stream_name == "order_completed":
                    print(f"Obaveštenje: Porudžbina {message.get('pk')} je uspešno kreirana i plaćena")
                elif stream_name == "refund_order":
                    print(f"Obaveštenje: Porudžbina {message.get('pk')} je refundirana")

    except Exception as e:
        print(f"Notification error: {e}")

    time.sleep(1)