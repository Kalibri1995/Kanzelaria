import smtplib


def send_order_by_email(order_info):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('kanzelariabot2021@gmail.com', 'web2021project')
    s.sendmail("kanzelariabot2021@gmail.com", "kanzelariabot2021@gmail.com", order_info)
    s.quit()
