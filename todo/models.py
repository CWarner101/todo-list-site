# Name: Connor Warner
# Class: CIS 218
# Date: 2/7/24

from django.db import models

class Todo(models.Model):
    name = models.TextField()
    complete_by = models.DateField()


    def __str__(self):
        """String method"""
        return self.name[:50]