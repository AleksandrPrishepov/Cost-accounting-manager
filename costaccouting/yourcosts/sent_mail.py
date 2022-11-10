from django.db.models import Count, Sum
from yourcosts.models import *
from django.core.mail import send_mail
import time
import schedule

count_tr = InfotmationTransaction.objects.values('user_id').annotate(Count('id'))
costs_summ = InfotmationTransaction.objects.values('user_id').annotate(Sum('costs_sum'))

def sent_mail():
    for user in User.objects.all():
        for j in range(len(count_tr)):
                if user.pk == count_tr[j]['user_id']:
                    static_data = f'''Количество затрат: {count_tr[j]['id__count']},
                                Сумма затрат: {round(costs_summ[j]['costs_sum__sum'])}'''
                    send_mail(
                        'Статистика ваших затрат',
                        static_data,
                        'sanyaprishepov@mail.ru',
                        [user.email],
                        fail_silently=False,
                )
                    break

schedule.every().day.at("21:18").do(sent_mail())

while True:
    schedule.run_pending()
    time.sleep(1)