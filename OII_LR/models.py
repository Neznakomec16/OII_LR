from typing import Iterable

from django.db import models


# Create your models here.
class Candidates(models.Model):
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    experience = models.FloatField(verbose_name='Опыт работы')
    age = models.FloatField(verbose_name='Возраст')
    experience_small = models.FloatField(blank=True, null=True)
    experience_middle = models.FloatField(blank=True, null=True)
    experience_big = models.FloatField(blank=True, null=True)
    age_small = models.FloatField(blank=True, null=True)
    age_middle = models.FloatField(blank=True, null=True)
    age_big = models.FloatField(blank=True, null=True)

    def set_affiliations(self, age: dict, experience: dict):
        self.experience_small = experience.get('small')
        self.experience_middle = experience.get('middle')
        self.experience_big = experience.get('big')
        self.age_small = age.get('small')
        self.age_middle = age.get('middle')
        self.age_big = age.get('big')

        return self

    def __repr__(self):
        return self.__str__()

    def __dir__(self) -> Iterable[str]:
        return f'<Candidate [age: {self.age}, experience: {self.experience}]>'
