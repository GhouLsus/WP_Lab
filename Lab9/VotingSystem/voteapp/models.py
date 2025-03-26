from django.db import models

class Vote(models.Model):
    choice_options = [
        ('Good', 'Good'),
        ('Satisfactory', 'Satisfactory'),
        ('Bad', 'Bad'),
    ]
    choice = models.CharField(max_length=20, choices=choice_options)
    
    def __str__(self):
        return self.choice
