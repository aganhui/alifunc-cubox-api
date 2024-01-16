import requests

def send_content_to_cubox(user_id, type, content, title, description, tags, folder):
    """
    Save content to Cubox using their API.
    
    :param type: The type of content to be saved. Can be 'url' or 'memo'.
    :param content: The content to be saved.
    :param title: Title for the saved content.
    :param description: Description for the saved content.
    :param tags: List of tags for the saved content.
    :param folder: The folder in which to save the content.
    :return: Response from the API call.
    """
    api_endpoint = f'https://cubox.pro/c/api/save/{user_id}'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'type': type,
        'content': content,
        'title': title,
        'description': description,
        'tags': tags,
        'folder': folder
    }
    response = requests.post(api_endpoint, json=payload, headers=headers)
    return response.json()

def save_content_to_cubox(user_id, type, content, title, description, tags, folder):
    """
    Save content to Cubox using their API.
    
    :param type: The type of content to be saved. Can be 'url' or 'memo'.
    :param content: The content to be saved.
    :param title: Title for the saved content.
    :param description: Description for the saved content.
    :param tags: List of tags for the saved content.
    :param folder: The folder in which to save the content.
    :return: Response from the API call.
    """
    if type not in ['url', 'memo']:
        return {"message": "Invalid type", "code": 400}
    if type == 'memo' and len(content) > 3000:
        return {"message": "Content exceeds 3000 characters", "code": 400}
    return send_content_to_cubox(user_id, type, content, title, description, tags, folder)
