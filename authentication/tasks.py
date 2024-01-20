from celery import shared_task
from django.core.mail import send_mail
from restaurantDiaryProject import settings


@shared_task(bind=True)
def send_email_func(self, email, token):

    mail_subject = "Talantoner"
    message = "Password reset email /api/reset-password/{token}".format(token=token)
    to_email = email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return "Done"
