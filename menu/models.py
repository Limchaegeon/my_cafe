from django.db import models

class Menu(models.Model):
  BIG="big"
  SMALL="small"
  SIZE_CHOICES=[
    (BIG,"Big"),
    (SMALL,"Small"),
  ]
  HOT="hot"
  ICE="ice"
  TEMP_CHOICES=[
    (HOT,"Hot"),
    (ICE,"Ice"),
  ]
  item = models.CharField(max_length=255)
  size = models.CharField(
    max_length=5,
    choices=SIZE_CHOICES,
    default=SMALL,
  )
  price = models.IntegerField(null=True)
  temp = models.CharField(
    max_length=3,
    choices=TEMP_CHOICES,
    default=HOT,
  )
  sajin=models.ImageField(upload_to = 'images/',null=True)
  #사진 복사 lms참고
  def __str__(self):
    return self.item

