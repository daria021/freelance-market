from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE


class Client(Model):
    full_name = CharField(max_length=50)
    nickname = CharField(max_length=30, unique=True)
    email = CharField(max_length=50)
    phone_number = CharField(max_length=50)

    def __str__(self):
        return self.nickname


class Executor(Model):
    full_name = CharField(max_length=50)
    nickname = CharField(max_length=30, unique=True)
    email = CharField(max_length=50)
    phone_number = CharField(max_length=50)
    specialization = CharField(max_length=50)
    experience = CharField(max_length=1000)

    def __str__(self):
        return f'{self.nickname}\n{self.specialization}\n{self.experience}'
