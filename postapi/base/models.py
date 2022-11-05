from django.db import models
from enum import Enum


class OperationType(Enum):
    AD = "addition"
    SU = "subtraction"
    MU = "multiplication"


class Question(models.Model):

    operation_type = models.CharField(max_length=100,
                                      choices=[(operation, operation.value)
                                               for operation in OperationType])
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)
    slackUsername = models.CharField(max_length=50,
                                     null=True,
                                     default='Creativity_TechGenius777')
    result = models.IntegerField(null=True, blank=True)
