def send_mail(msg, receiver, sender='KOOBSCOLABS@gmail.com'):
  '''Usage: send_mail(msg,receiver,sender=KOOBSCOLABS@gmail.com)'''
  import smtplib
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("KOOBSCOLABS@gmail.com", "0O9i8u7y!")
  server.sendmail(sender, receiver, msg)
  server.quit()
