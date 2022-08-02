from django.core.mail import send_mail

def send(user_email, name, task_description):
    send_mail(
        'Время на выполнение задачи вышло',
        f"Уважаемый(-ая) {name}, дедлайн для задачи \"{task_description}\" пройден.",
        'noreplydjangocelery@gmail.com',
        [user_email],
        fail_silently=False,
    )
