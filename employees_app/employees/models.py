from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30, )
    last_name = models.CharField(max_length=40, null=True, blank=True, default='NO NAME', )
    egn = models.CharField(max_length=10, unique=True, )
    job_title = models.CharField(
        max_length=40,
        choices=(
            ('Software developer', 1),
            ('QA Engineer', 2),
            ('DevOps', 3),
        )
    )
