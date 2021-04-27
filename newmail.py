# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("fypsamveera@gmail.com", "fypsamveera123")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("fypsamveera@gmail.com", "rodinjack9@gmail.com", message)
  
# terminating the session
s.quit()