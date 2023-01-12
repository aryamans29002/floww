from django.db import models

# Create your models here.

class ErrorLogApi(models.Model):
    id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=CHAR_SIZE_MEDIUM)
    error_val = models.CharField(max_length=CHAR_SIZE_MEDIUM)
    timestamp = models.CharField(max_length=CHAR_SIZE_MEDIUM)
    user_id = models.CharField(max_length=CHAR_SIZE_MEDIUM)


class UsageLogApi(models.Model):
    id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=CHAR_SIZE_MEDIUM)
    api_success = models.BooleanField(default=True)
    timestamp = models.CharField(max_length=CHAR_SIZE_MEDIUM)
    user_id = models.CharField(max_length=CHAR_SIZE_MEDIUM)