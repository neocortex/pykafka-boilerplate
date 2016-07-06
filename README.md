# pykafka-boilerplate

**Boilerplate code for a pykafka**

Instructions:

    - [Download](http://kafka.apache.org/downloads.html) Kafka
    - `pip` Install [pykafka](https://github.com/Parsely/pykafka)
    - Start the Zookeeper server

        bin/zookeeper-server-start.sh config/zookeeper.properties

    - Start the Kafka server

        bin/kafka-server-start.sh config/server.properties

    - Send some messages

        python producer_test.py

    - Consume the messages

        python consumer_test.py

See [here](http://kafka.apache.org/07/quickstart.html) for more information.
