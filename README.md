
send content to cubox by cubox-user-api & deploy to aliyun faas

# deploy to aliyun faas
TODO

# invoke params

body format:

```
{
    "user_id": "your cubox api id",
    "type": "url",
    "content": "http://test.com",
    "title": "Example Title",
    "description": "This is an example description for the URL.",
    "tags": [
        "example",
        "test",
        "url"
        ],
    "folder": "Test Folder"
}
```