from django.db import models


class Account(models.Model):
    signin_id = models.CharField(db_column='signin_id', max_length=50)
    signin_pw = models.IntegerField(db_column='signin_pw')

    class Meta:
        db_table = 'accounts'
