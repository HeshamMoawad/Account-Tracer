from django.db import models
from colorfield.fields import ColorField





class Project(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, unique=True)
    imgURL = models.ImageField( upload_to='projects-images/', max_length=None , null=True)
    color = ColorField(verbose_name='Color')
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class Agent(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, unique=True)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True )
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'



class TwitterAccount(models.Model):
    handle = models.CharField(verbose_name="Handle", max_length=50)
    password = models.CharField(verbose_name="Password", max_length=50)
    agent = models.ForeignKey(Agent , on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True, )

    def __str__(self) -> str:
        return f"{self.handle} - Created at {self.created_datetime}"

    class Meta:
        verbose_name = 'Twitter Account'
        verbose_name_plural = 'Twitter Accounts'




class AccountLoginInfo(models.Model):
    account = models.ForeignKey(TwitterAccount,on_delete=models.CASCADE)
    id_str = models.CharField(verbose_name="ID", max_length=50, unique=True)
    rest_id = models.CharField(verbose_name="Rest ID", max_length=50)
    name = models.CharField(verbose_name="Name", max_length=50)
    screen_name = models.CharField(verbose_name="Handle", max_length=50)
    description = models.TextField(verbose_name='Bio' ,max_length=300)
    verified = models.BooleanField(verbose_name="Verified", default=False)
    cookies = models.CharField(verbose_name="Cookies", max_length=500)
    token = models.CharField(verbose_name="Token", max_length=300)
    suspend = models.BooleanField(verbose_name="Suspension Status", default=False)
    created_at = models.CharField(verbose_name="Created At", max_length=60)
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - Created at {self.created_datetime}"

    class Meta:
        verbose_name = 'Account Login Info'
        verbose_name_plural = 'Accounts Login Info'



class Tweet(models.Model):
    conversation_id_str = models.CharField(verbose_name="ID", max_length=50, unique=True)
    favorite_count = models.IntegerField(verbose_name="Likes Count")
    reply_count = models.IntegerField(verbose_name="Replies Count")
    retweet_count = models.IntegerField(verbose_name="Retweet Count")
    user_id_str = models.CharField(verbose_name="ID", max_length=50)
    bookmark_count =  models.IntegerField(verbose_name="BookMarked Count")
    full_text = models.TextField(verbose_name="Body")
    created_at = models.CharField(verbose_name="Created At", max_length=60)
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'


