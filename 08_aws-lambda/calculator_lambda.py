import json


def lambda_handler(event, context):

    first_number = event['queryStringParameters']['firstNumber']
    second_number = event['queryStringParameters']['secondNumber']
    operand = event['queryStringParameters']['operand']

    result = []
    if (operand == 'add'):
        result['total'] = first_number + second_number

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
