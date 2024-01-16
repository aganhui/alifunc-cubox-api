import json
import cgi

def parse_request_body_form_data(request_body):
    boundary = request_body.splitlines()[0]
    parts = request_body.split(boundary)

    form_data = {}
    for part in parts:
        if part and "Content-Disposition" in part:
            header, value = part.split("\r\n\r\n", 1)
            field_name = header.split('name="')[1].split('"')[0]
            form_data[field_name] = value.strip()

    return form_data

def parse_wsgi_input(environ):
    content_type = environ.get('CONTENT_TYPE', '').lower()
    request_body_size = int(environ.get('CONTENT_LENGTH', 0) or 0)
    request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')

    if 'application/json' in content_type:
        return json.loads(request_body)
    elif 'application/x-www-form-urlencoded' in content_type:
        return cgi.parse_qs(request_body)
    elif 'multipart/form-data' in content_type:
        return parse_request_body_form_data(request_body)
    else:
        return request_body
    
def parse_wsgi_environ(environ):
    # Extracting essential information from the environ dictionary
    parsed_environ = {
        "request_method": environ.get('REQUEST_METHOD'),
        "script_name": environ.get('SCRIPT_NAME'),
        "path_info": environ.get('PATH_INFO'),
        "query_string": environ.get('QUERY_STRING'),
        "content_type": environ.get('CONTENT_TYPE'),
        "content_length": environ.get('CONTENT_LENGTH'),
        "server_name": environ.get('SERVER_NAME'),
        "server_port": environ.get('SERVER_PORT'),
        "http_host": environ.get('HTTP_HOST'),
        "http_user_agent": environ.get('HTTP_USER_AGENT'),
        "http_cookie": environ.get('HTTP_COOKIE'),
        "wsgi_version": environ.get('wsgi.version'),
        "wsgi_url_scheme": environ.get('wsgi.url_scheme'),
        "wsgi_input": environ.get('wsgi.input'),
        "wsgi_errors": environ.get('wsgi.errors'),
        "wsgi_multithread": environ.get('wsgi.multithread'),
        "wsgi_multiprocess": environ.get('wsgi.multiprocess'),
        "wsgi_run_once": environ.get('wsgi.run_once'),
        "request_body": parse_wsgi_input(environ),
    }

    # Optional: Parse and add custom headers
    custom_headers = {}
    for key, value in environ.items():
        if key.startswith("HTTP_"):
            custom_headers[key] = value
    parsed_environ['custom_headers'] = custom_headers

    return parsed_environ

def print_parsed_environ(parsed_environ):
    for key, value in parsed_environ.items():
        print(f"{key}: {value}")

def print_wsgi_environ(environ):
    for key, value in environ.items():
        # Since some values in environ could be non-string (like wsgi.input), 
        # we ensure they are properly converted to strings for printing.
        if key == 'wsgi.input':
            # For 'wsgi.input', you might want to read a portion of it
            # or avoid printing it entirely as it can be a large stream of data.
            print(f"{key}: <wsgi.input stream>")
        elif key == 'wsgi.errors':
            # Similarly, 'wsgi.errors' is a stream for error logging
            print(f"{key}: <wsgi.errors stream>")
        else:
            print(f"{key}: {value}")