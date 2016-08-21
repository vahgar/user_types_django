from accounts.models import User_type_1
from django.contrib.auth.hashers import check_password

class User_type_1_AUTH(object):
    def authenticate (self, username=None, password=None):
        try:
            user = User_type_1.objects.get(username=username)
            if user.check_password(password):
                print('yo')
                return user

            else:
                return None

        except User_type_1.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User_type_1.objects.get(pk=user_id)
        except User_type_1.DoesNotExist:
            return None
