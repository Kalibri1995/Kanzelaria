import smtplib
from email.header import Header
from email.mime.text import MIMEText
from Kanzelaria import models
from ..models.order_frontend import OrderFrontend


def send_order_by_email(order_info, request):
    msg = MIMEText(get_msg(order_info, request), 'plain', 'utf-8')
    msg['Subject'] = Header(f'Заказ №{order_info.id}', 'utf-8')

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('kanzelariabot2021@gmail.com', 'web2021project')
    s.sendmail("kanzelariabot2021@gmail.com", "kanzelariabot2021@gmail.com", msg.as_string())
    s.quit()


def get_msg(order_info, request):
    msg = "Поступил новый заказ: \n" + \
        str(order_info) + "\n\n" + \
        "Все заказы: \n"

    orders = request.dbsession.query(models.Order).all()
    for order_db in orders:
        order_f = OrderFrontend(
            request,
            order_db.id,
            order_db.name,
            order_db.phone,
            order_db.sum,
            order_db.shop_id,
            order_db.products
        )
        msg += str(order_f) + "\n"

    return msg