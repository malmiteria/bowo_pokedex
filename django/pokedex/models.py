from django.db import models


class Pokemon(models.Model):
    attack = models.IntegerField()
    classification = models.CharField(db_column="classfication", max_length=255)
    defense = models.IntegerField()
    height_m = models.FloatField(blank=True, null=True)
    hp = models.IntegerField()
    japanese_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    pokedex_number = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255, blank=True, null=True)
    weight_kg = models.FloatField(blank=True, null=True)
    generation = models.IntegerField()
    is_legendary = models.BooleanField()

