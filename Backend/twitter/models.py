from django.db import models
# from core.utils import getToken , getUserID
# Create your models here.


class TwitterAccount(models.Model):
    id_str = models.CharField(verbose_name="ID",max_length=50 , unique=True)
    rest_id = models.CharField(verbose_name="ID",max_length=50)
    name = models.CharField(verbose_name="Name" , max_length=50 , null=True)
    handle = models.CharField(verbose_name="Handle" , max_length=50)
    cookies = models.CharField(verbose_name="Cookies", max_length=300)
    suspend = models.BooleanField(verbose_name="Suspension Status",default=False)
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date" , auto_now=True)

    # @property
    # def token (self)->str:
    #     return getToken(self.cookies)

    # @property
    # def user_id (self)->str:
    #     return getUserID(self.cookies)
        
    def __str__(self) -> str:
        return f"{self.handle} - {self.name} - Created at {self.created_datetime}"

    class Meta:
        verbose_name = 'TwitterAccount'
        verbose_name_plural = 'TwitterAccounts'



class AccountRecord(models.Model):
    account = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE)
    tweets_count = models.IntegerField(verbose_name="Tweets Count")
    replys_count = models.IntegerField(verbose_name="Replys Count")
    messages_count = models.IntegerField(verbose_name="Messages Count")
    followers_count = models.IntegerField(verbose_name="Followers Count")
    following_count = models.IntegerField(verbose_name="Following Count")
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date" , auto_now=True)

    def __str__(self) -> str:
        return f"{self.account.handle} - Updated at {self.updated_datetime}"

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'




