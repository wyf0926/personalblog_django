from users.models import EmailVerification
from django.core.mail import send_mail
import random
import string


def random_str(length=8):
    """Randomly generate a string of length 8"""
    chars = string.ascii_letters + string.digits  # generate a-zA-Z0-9
    code = ''.join(random.sample(chars, length))  # actual 8-bits verification code
    return code


def send_register_email(email, send_type='register'):
    email_record = EmailVerification()
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = 'Yifan\'s Personal Blog Verification Link'
        email_body = 'Please click on the following link to activate your account:' \
                     ' http://127.0.0.1:8000/users/activate/{0}'.format(code)
        send_status = send_mail(email_title, email_body, 'yanzuece@foxmail.com', [email])
        if send_status:
            pass
