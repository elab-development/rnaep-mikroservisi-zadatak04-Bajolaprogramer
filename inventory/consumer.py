from database import redis
from main import Product
import time

key = 'order_completed'

while True:
    try:
        results = redis.xread({key: '0'}, count=1, block=5000)

        if results:
            for result in results:
                message_id = result[1][0][0]
                obj = result[1][0][1]

                print("PROCITAO SAM PORUKU:", obj)

                try:
                    product = Product.get(obj['product_id'])
                    product.quantity -= int(obj['quantity'])
                    product.save()

                    print(f"Stock updated for {product.name}")

                except Exception as e:
                    print(f"Error: {e}")

    except Exception as e:
        print(str(e))

    time.sleep(1)