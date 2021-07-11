from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import OuterRef, F


class UserManager(BaseUserManager):
    def create_user(self, login, bank, password=None,  is_staff=False, is_superuser=False,):
        if not login:
            raise ValueError('Users must have login')
        if not password:
            raise ValueError('Must have pas')
        if not bank:
            raise ValueError('bank>???')
        user = self.model(
            login=login,
            bank=bank,

        )
        user.is_staff = is_staff
        user.is_superuser = is_superuser

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, login, bank, password=None):
        user = self.create_user(
            login=login,
            bank=bank,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, login, bank, password=None):
        user = self.create_user(
            login=login,
            bank=bank,
            password=password,
            is_staff=True,
            is_superuser=True,
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    bank = models.FloatField()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'login'
    objects = UserManager()

    def __str__(self):
        return self.login


class Bet(models.Model):
    name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    total_sum = models.FloatField()
    coefficient = models.FloatField(validators=[MinValueValidator(1)])
    result = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    @property
    def get_profit(self):
        if self.result is True:
            return round(self.total_sum * (self.coefficient - 1), 2)

        else:
            return -self.total_sum

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(Bet, self).save(*args, **kwargs)
        if created:
            User.objects.filter(id=self.user_id).update(
                bank=F('bank') + self.get_profit)

    def __str__(self):
        return self.name

