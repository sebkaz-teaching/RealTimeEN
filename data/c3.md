
## Apache Kafka
Producent kafka
```python
import json
import random
import sys
from datetime import datetime, timedelta
from time import sleep

from kafka import KafkaProducer


if __name__ == "__main__":
    server = sys.argv[1] if len(sys.argv) == 2 else "localhost:9092"

    producer = KafkaProducer(
        bootstrap_servers=[server],
        value_serializer=lambda x: json.dumps(x).encode("utf-8"),
        api_version=(2, 7, 0),
    )

    try:
        while True:
            message = {
                "time": str(
                    datetime.now() + timedelta(seconds=random.randint(-15, 0))
                ),
                "id": random.choice(["a", "b", "c", "d", "e"]),
                "value": random.randint(0, 100),
            }
            producer.send("topicX", value=message)
            sleep(1)
    except KeyboardInterrupt:
        producer.close()
```


ZMIEŃ KATALOG
```bash
cd kafka_2.12-2.7.0
```

WYKONAJ - terminal 1 - start zookeepera
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

WYKONAJ - terminal 2 - start serwera kafki
```bash
bin/kafka-server-start.sh config/server.properties
```

WYKONAJ - terminal 3 - stworzenie tematu X
```bash
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic topicX

```

WYKONAJ - terminal 4 - start producera
```bash
python producer.py
```

