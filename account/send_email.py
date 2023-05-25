from django.core.mail import send_mail
from product.models import Product

def send_confirmation_email(user, code):
    code = user.activation_code
    code = code 
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}/'
    to_email = user.email
    to_email = user
    send_mail('Здраствуйте активируйте ваш аккаунт', f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
    'izzatulla.biibek@gmail.com', [to_email,], fail_silently=False)

def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Subject',
        f'Your code for reset password:{code}',
        'from@example.com',
        [to_email,],
        fail_silently=False
    )

def send_notification(user, id):
    to_email = user.email
    send_mail(
        'Уведомление о создании заказов!',
        f'Вы создали заказ N:{id}, ожидайте звонка!',
        'from@example.com',
        [to_email,],
        fail_silently=False
    )

def send_html_email():
    from django.template.loader import render_to_string
    product = Product.objects.all()[0]
    html_message = render_to_string('f.html', {'name': product.title, 'description': product.description})
    send_mail(
        'Subject',
        'pismo Manasu-chychkaky',
        'example@admin.com',
        ['Turatbaevmanas94@gmail.com'],
        html_message=html_message,
        fail_silently=False
    )