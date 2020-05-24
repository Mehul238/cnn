import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("mehul20042001@gmail.com", "M8107922492")
server.sendmail("mehul20042001@gmail.com",
                "mehul20042000@gmail.com",
                "jon is successful")
server.quit()