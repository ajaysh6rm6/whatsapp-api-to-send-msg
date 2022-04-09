#REQUIREMENTS 

#twilio-6.62.1
#APScheduler-3.7.0
#django-3.2.6


from twilio.rest import Client 
 
account_sid = '*************************' 
auth_token = '*************************' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hi this msg only testing purpose....bye',      
                              to='whatsapp:+919********7' 
                          ) 
 
print(message.sid)
