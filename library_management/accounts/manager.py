from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if username is None or email is None:
            raise ValueError('Username and email are required')
        user = self.model(
            username = username.lower(),
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        # user.save(using = self._db) # that _db used for when you have multiple databases, and need to assign one explecitly 
        user.save()
        return user