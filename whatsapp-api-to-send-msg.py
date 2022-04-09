#REQUIREMENTS 

#twilio-6.62.1
#APScheduler-3.7.0
#django-3.2.6


from twilio.rest import Client 
 
account_sid = 'AC479490a9eaa13000e4faf57e5878ca30' 
auth_token = '202cf9d5d5aca559797ff746aefda3df' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='hi this msg only testing purpose....bye',      
                              to='whatsapp:+919********7' 
                          ) 
 
print(message.sid)