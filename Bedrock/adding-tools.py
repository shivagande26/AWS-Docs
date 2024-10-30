import datetime
import json

def lambda_handler(event, context):
    agent = event['agent']
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])

    # Execute your business logic here. For more information, refer to: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    # responseBody =  {
    #     "TEXT": {
    #         "body": "The function {} was called successfully!".format(function)
    #     }
    # }

    def get_time():
        return datetime.datetime.utcnow().strftime('%H:%M:%S')

    result = get_time()
    result_text = "The time is {}".format(result)
    responseBody = {
        "TEXT": {
            "body": result_text
        }
    }

    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }
    }

    dummy_function_response = {'response': action_response, 'messageVersion': event['messageVersion']}
    print("Response: {}".format(dummy_function_response))
    return dummy_function_response