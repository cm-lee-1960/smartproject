from django.db import models

# Create your models here.
# class Restapp(models.Model):
#     number = models.CharField(primary_key=True, max_length=50)
#     boot = models.CharField(max_length=10)
#     address = models.CharField(max_length=50, blank=True, null=True)
#     m_rsrp = models.IntegerField(blank=True, null=True)
#     dl_th = models.IntegerField(blank=True, null=True)
#     ul_th = models.IntegerField(blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         #managed = False
#         #db_table = 'smart'
#         ordering = ['created']

class Restapp(models.Model):
    num = models.IntegerField(primary_key=True)
    phonenumber = models.CharField(max_length=50)
    boot = models.CharField(max_length=10)
    address = models.CharField(max_length=50, null=True)
    m_rsrp = models.IntegerField(null=True)
    dl_th = models.IntegerField(null=True)
    ul_th = models.IntegerField(null=True)

    # class Meta:
    #     managed = False
    #     db_table = 's_cxi'

        
# class Restapp2(models.Model):
#     number = models.CharField(primary_key=True, max_length=50)
#     boot = models.CharField(max_length=10)
#     address = models.CharField(max_length=50, blank=True, null=True)
#     #m_rsrp = models.IntegerField(blank=True, null=True)
#     #dl_th = models.IntegerField(blank=True, null=True)
#     #ul_th = models.IntegerField(blank=True, null=True)
#     #created = models.DateTimeField(auto_now_add=True)

#     #class Meta:  # 내부클래스
#         #managed = False
#         #db_table = 'smart'
#         #ordering = ['created']
    
    def __str__(self):
        return self.address