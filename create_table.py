import boto3

# Simple API call to Dynamo to create a table
client = boto3.client('dynamodb', region_name='us-east-1')

try:
    resp = client.create_table(
        TableName="Customers",
        # Declare your Primary Key in the KeySchema argument
        KeySchema=[
            {
                "AttributeName": "account_id",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "task_id",
                "KeyType": "RANGE"
            }
        ],
        # Any attributes used in KeySchema or Indexes must be declared in AttributeDefinitions
        AttributeDefinitions=[
            {
                "AttributeName": "account_id",
                "AttributeType": "S"
            },
            {
                "AttributeName": "task_id",
                "AttributeType": "S"
            }
        ],
        # ProvisionedThroughput controls the amount of data you can read or write to DynamoDB per second.
        # You can control read and write capacity independently.
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        }
    )
    print("Table created successfully!")
except Exception as e:
    print("Error creating table:")
    print(e)
