# from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
from time import sleep
import smtplib

# twilio_account_sid = 'AC716250b5c85290dfa469d73254129deb'
# twilio_auth_token = 'b2eaf28bd120398ab1cf8357d38b49ee'

# def send_whatsapp_message(to_number, message):
#     client = Client(twilio_account_sid, twilio_auth_token)
#     message = client.messages.create(
#         body=message,
#         from_="+12295454807",
#         to='whatsapp:' + '+923485947677'
#     )
#     print('WhatsApp Message Sent!')
#     # Send SMS message using Twilio API


# def send_sms(to_number, message):
#     client = Client(twilio_account_sid, twilio_auth_token)
#     message = client.messages.create(
#         body=message,
#         from_="+12295454807",  # Use the same Twilio number for SMS
#         to='+923485947677'
#     )
#     print('SMS Sent!')


url = "https://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

email_count = 0

while True:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')  # Converts to BeautifulSoup Object
    select_element = soup.select('select[name="fields[3].content"]')
    options = select_element[0].find_all('option')

    # twilio recovery code

    # 8YJBWZ1CGNWZMGDCLSYXT4RG

    # search_text = {'winter','winter semester', 'winter semester 2023', '2023'}
    search_text = {"summer","summer semester", "summer semester 2024", "2024"}
    send_email = False
    for option in options:
        # print(options.index(option)+1,option['value'],"\n", option.text)
        for x in search_text:
            if(option.text.find(x) != -1):
                print("\n-------------------- ",x,"----------------------- \n")
                send_email = True
    if(send_email != True):
        print("NOT FOUND \n")
    else:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("jamillaghari2000@gmail.com", "dmqb xkcd yikn ewtb")
        message = "The appointments for germany are open please go to this website to fill for me \nhttps://service2.diplo.de/rktermin/extern/appointment_showForm.do?locationCode=isla&realmId=108&categoryId=1600 \npassport no: KA6919401 telephone: 03485947677"
        s.sendmail("jamillaghari2000@gmail.com", "jamillaghari2000@gmail.com", message)
        # intizarlaghari@gmail.com
        s.sendmail("jamillaghari2000@gmail.com", "intizarlaghari@gmail.com", message)
        # Abrarlaghari@hotmail.com
        s.sendmail("jamillaghari2000@gmail.com", "Abrarlaghari@hotmail.com", message)
        s.sendmail("jamillaghari2000@gmail.com", "lgharizahra@gmail.com", message)

        # Import the required libraries
        # Twilio API credentials

        # twilio_whatsapp_number = '+923485947677'

        # Usage examples
        # send_whatsapp_message('+923485947677', message)
        # send_sms('+923485947677', message)


        s.quit()
        email_count += 1
        print("\n-------------------- FOUND ----------------------- \n")
        if email_count > 5:
            break
    sleep(10)
