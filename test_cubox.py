from cubox import save_url_to_cubox, save_memo_to_cubox

user_id = "a0uuqw7rU9i"

def test_save_url_to_cubox():
    # Example data for testing save_url_to_cubox function
    test_url = 'https://www.example.com'
    test_title = 'Example Title'
    test_description = 'This is an example description for the URL.'
    test_tags = ['example', 'test', 'url']
    test_folder = 'Test Folder'

    # Call the save_url_to_cubox function with example data
    result = save_url_to_cubox(user_id, test_url, test_title, test_description, test_tags, test_folder)
    
    # Print the result
    print('Test save_url_to_cubox result:', result)
    return result

def test_save_memo_to_cubox():
    # Example data for testing save_memo_to_cubox function
    test_content = 'This is an example content for the memo, which should not exceed 3000 characters.'
    test_title = 'Example Memo Title'
    test_description = 'This is an example description for the memo.'
    test_tags = ['example', 'test', 'memo']
    test_folder = 'Test Memo Folder'

    # Call the save_memo_to_cubox function with example data
    result = save_memo_to_cubox(user_id, test_content, test_title, test_description, test_tags, test_folder)
    
    # Print the result
    print('Test save_memo_to_cubox result:', result)
    return result

# Note: These tests will actually perform API calls. Ensure that the API endpoint and API key are correct and that you have permission to use the API for testing.
