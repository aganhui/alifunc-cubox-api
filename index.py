HELLO_WORLD = b"Hello world! ygh abcd\n"

from utils import parse_wsgi_environ, print_parsed_environ
from cubox import save_content_to_cubox

def handler(environ, start_response):
    context = environ['fc.context']
    request_uri = environ['fc.request_uri']
    for k, v in environ.items():
        if k.startswith("HTTP_"):
            # process custom request headers
            pass

    parsed_environ = parse_wsgi_environ(environ)
    request_body = parsed_environ['request_body']
    result = save_content_to_cubox(request_body['user_id'], request_body['type'], request_body['content'], request_body['title'], request_body['description'], request_body['tags'], request_body['folder'])

    # Check the result and set the status accordingly
    if result['code'] == 200:
        status = '200 OK'
        response_body = 'Content saved successfully.\n'
    else:
        status = '400 Bad Request'
        response_body = f"Failed to save Content. Error code: {result['code']}. Message: {result['message']}\n"

    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    
    # return value must be iterable, so we convert the response_body to bytes and put it in a list
    return [response_body.encode('utf-8')]
