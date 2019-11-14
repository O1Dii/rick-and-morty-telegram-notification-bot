from app import dynamodb, table


def delete_from_db(chat_id):
    table.delete_item(Key={'chat_id': chat_id})


def add_to_db(chat_id):
    table.put_item(Item={'chat_id': chat_id})


def create_table(name):
    return dynamodb.create_table(
        TableName=name,
        KeySchema=[
            {
                'AttributeName': 'chat_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'chat_id',
                'AttributeType': 'N'
            }
        ],
        BillingMode='PAY_PER_REQUEST'
    )
