#Luis Baez and Izzy Hurley
#cs431 networks
#Purpose: send an email alerting people that the temperature is too high from #colby.ferment.club@gmail.com

import smtplib
from email.message import EmailMessage

#send the alert to recipient, and use currentTemp and desiredTemp create message
def sendAlert(recipient: str, currentTemp: int, desiredTemp: int):
    #set the smtp server and port to be used, use secure connection (required)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #I left password here as this account is only for this project
    server.login('colby.ferment.club@gmail.com', 'colbyferment23')

    #create the message object, set origin, contents, subject and destination, then send
    msg = EmailMessage()
    msg['From'] = 'colby.ferment.club@gmail.com'

    #use the temperature to create the message for too hot or two cold
    tempDelta = currentTemp - desiredTemp
    #if this was accidentaly called exit
    if tempDelta == 0:
        server.quit()
        print("Message cancelled")
        return
    elif tempDelta > 0:
        msg['Subject'] = 'Temperature High'
        msg.set_content(f"Product is {tempDelta} degrees Celcius too hot\n\nCurrent temperature: {currentTemp} degrees Celcius")
    elif tempDelta < 0:
        msg['Subject'] = 'Temperature Low'
        msg.set_content(f"Product is {abs(tempDelta)} degrees Celcius too cold\n\nCurrent temperature: {currentTemp} degrees Celcius")
    
    #could change later to ferment club email list or multiple people

    msg['To'] = recipient
    
    server.send_message(msg)
    server.quit()

def main():
    email= input("plese enter an email to send alerts to:")
    sendAlert(email, 85, 78)

if __name__ == "__main__":
    main()

