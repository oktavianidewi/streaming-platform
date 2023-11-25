import datetime
import random

STREAM_NAME = "StockSampleStream"


def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': round(random.random() * 100, 2)
    }


def generate(stream_name):
    while True:
        data = get_data()
        print(data)
        # kinesis_client.put_record(
        #     StreamName=stream_name,
        #     Data=json.dumps(data),
        #     PartitionKey="partitionkey")


if __name__ == '__main__':
    generate(STREAM_NAME)