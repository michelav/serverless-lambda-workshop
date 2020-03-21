import json
import logging

def helloPath(event, context):
    """Parses a pathParam parameter from URL path

    GET /hello/{pathParam}
    """

    name = event['pathParameters']['pathParam']

    # TODO Handle URL encoded characters

    response = {
        "message": f"Hello from HelloPath Function: {name}"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response),
         "headers": {
            "Content-Type": "application/json"
        }
    }

def helloQuery(event, context):
    """Parses a variable qParam from Query String

    GET /hello?q={qParam}
    """

    name = event['queryStringParameters']['qParam']

    # TODO Handle URL encoded characters

    response = {
        "message": f"Hello {name} from HelloQuery Function!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response),
         "headers": {
            "Content-Type": "application/json"
        }
    }

def helloPost(event, context):
    """Handles a POST JSON message containing a name attribute

    POST /hello_post
    """

    data = json.loads(event['body'])
    if 'name' not in data:
        logging.error("Could not find name variable in post msg")
        raise Exception("Couldn't find name variable.")

    name = data['name']

    # TODO Handle URL encoded characters

    response = {
        "message": f"Hello {name} from HelloPost Function!"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response),
         "headers": {
            "Content-Type": "application/json"
        }
    }