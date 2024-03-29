from django.db import models
# # Create your models here.

# class Leaderboard(models.Model):
#   name = models.CharField(max_length=200, null=False, default="")
#   email = models.EmailField(max_length=200, null=False, default="")
#   level = models.PositiveIntegerField(null=False, default=1)
#   score = models.IntegerField(null=False, default=0)
#   picture = models.CharField(max_length=200, null=True)

#   def __str__(self):
#     return self.email


class Question(models.Model):
  id = models.IntegerField(primary_key=True)
  question = models.CharField(max_length=500, null=False)
  answer = models.CharField(max_length=20, null=False)

  def __str__(self):
    return self.question


class Player(models.Model):
  name = models.CharField(max_length=200, null=False, default="")
  email = models.EmailField(max_length=200, null=False, default="")
  picture = models.CharField(max_length=200, null=True)
  isTeamed = models.BooleanField(default=False)

  def __str__(self):
    return self.email


class TeamLeaderboard(models.Model):
  teamName = models.CharField(max_length=50, null=False, default="")
  teamCode = models.CharField(max_length=6, null=False, unique=True)
  teamLevel = models.PositiveIntegerField(null=False, default=1)
  teamScore = models.IntegerField(null=False, default=0)
  teamLeader = models.OneToOneField(Player, on_delete=models.CASCADE, related_name="teamLeader")
  teamPlayerOne = models.OneToOneField(Player, on_delete=models.DO_NOTHING, related_name="teamPlayerOne", null=True, blank=True)
  teamPlayerTwo = models.OneToOneField(Player, on_delete=models.DO_NOTHING, related_name="teamPlayerTwo", null=True, blank=True)

  def __str__(self):
    return self.teamCode

class Rules(models.Model):
  rule = models.CharField(max_length=200, null=False, default="")

  def __str__(self):
    return self.rule