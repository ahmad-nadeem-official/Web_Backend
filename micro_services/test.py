import requests

BASE_URL = 'http://127.0.0.1:5000'

# def test_newsletter_subscription():
#     url = 'http://127.0.0.1:5000/subscribe'
#     data = {
#         'email': 'ahmadnadee@example.com'
#     }
#     response = requests.post(url, json=data)
#     print("📬 Newsletter Subscription")
#     print("Status Code:", response.status_code)
#     try:
#         print("Response:", response.json())
#     except Exception as e:
#         print("Response Error:", e)

# def test_meeting_schedule():
#     url = 'http://127.0.0.1:5000/meeting'
#     data = {
#         'name': 'John Doe',
#         'email': 'ahmadnadeem701065@gmail.com',
#         'date': '2023-10-01T14:30',  # ISO format (YYYY-MM-DDTHH:MM)
#         'message': 'This is a test message for meeting subscription.'
#     }
#     response = requests.post(url, json=data)
#     print("📅 Meeting Scheduling")
#     print("Status Code:", response.status_code)
#     try:
#         print("Response:", response.json())
#     except Exception as e:
#         print("Response Error:", e)

def test_contact_message():
    url = f'{BASE_URL}/contact'
    data = {
        'name': 'Jane Doe',
        'email': 'jane@emailcom',
        'subject': 'Test Subject',
        'message': 'This is a test message for contact.'
    }
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    try:
        print("Response:", response.json())
    except Exception as e:
        print("Response Error:", e)

if __name__ == '__main__':
    test_contact_message()
    # test_newsletter_subscription()
    # print()
    # test_meeting_schedule()
