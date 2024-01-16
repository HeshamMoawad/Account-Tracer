from django.db import models
from colorfield.fields import ColorField




class Project(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50, unique=True)
    imgURL = models.ImageField( upload_to='./twitter/projects-images/', max_length=None , null=True)
    color = ColorField(verbose_name='Color')
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class Agent(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    project = models.ForeignKey(Project , on_delete=models.SET_NULL , null=True )
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True )
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.project}"

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'



class TwitterAccount(models.Model):
    handle = models.CharField(verbose_name="Handle", max_length=50 , unique=True)
    password = models.CharField(verbose_name="Password", max_length=50)
    agent = models.ForeignKey(Agent , on_delete=models.SET_NULL , null=True )
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True, )

    def __str__(self) -> str:
        return f"{self.handle} - {self.agent} - Created at {self.created_datetime.date()}"

    class Meta:
        verbose_name = 'Twitter Account'
        verbose_name_plural = 'Twitter Accounts'



class AccountLoginInfo(models.Model):
    account = models.ForeignKey(TwitterAccount,on_delete=models.CASCADE , null=True )
    rest_id = models.CharField(verbose_name="Rest ID", max_length=50)
    name = models.CharField(verbose_name="Name", max_length=50)
    screen_name = models.CharField(verbose_name="Screen Name", max_length=50 , unique=True)
    description = models.TextField(verbose_name='Bio' ,max_length=300)
    profileImgURL = models.URLField(verbose_name="ImgURL")
    verified = models.BooleanField(verbose_name="Verified", default=False)
    cookies = models.CharField(verbose_name="Cookies", max_length=500)
    token = models.CharField(verbose_name="Token", max_length=300)
    suspend = models.BooleanField(verbose_name="Suspension Status", default=False)
    created_at = models.DateTimeField(verbose_name="Created At")
    ## not add when define new instance
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.screen_name} - Created at {self.created_datetime.date()}"

    class Meta:
        verbose_name = 'Account Login Info'
        verbose_name_plural = 'Accounts Login Info'



class Chat(models.Model):
    account = models.ForeignKey(TwitterAccount,on_delete=models.SET_NULL , null=True )
    conversation_id = models.CharField(verbose_name="Conversation ID", max_length=50)
    chat_datetime = models.DateTimeField(verbose_name="Chat Date & Time")
    status = models.CharField(verbose_name="Status", max_length=50)

    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.chat_datetime.date()} - {self.conversation_id} - {self.status}"

    class Meta:
        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

class FollowUnFollow(models.Model):
    account = models.ForeignKey(TwitterAccount,on_delete=models.SET_NULL , null=True )
    followers = models.IntegerField(verbose_name="Followers Count")
    following = models.IntegerField(verbose_name="Following Count")
    likes = models.IntegerField(verbose_name="Likes Count" , null=True)
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.account.handle} - Followers {self.followers} - Following {self.following} - {self.created_datetime}"
    class Meta:
        verbose_name = 'Follower & Following Count'
        verbose_name_plural = 'Follower & Following Counts'


class MediaLink(models.Model):
    class Type(models.TextChoices):
        VIDEO = 'video', 'Video'
        IMAGE = 'image', 'Image'
    url = models.URLField(verbose_name="Media URL" , unique=True)
    type = models.CharField(
        max_length= 20 ,
        choices=Type.choices,
        default= Type.IMAGE ,
    )
    def __str__(self) -> str:
        return f"{self.url}"

class Tweet(models.Model):
    account = models.ForeignKey(TwitterAccount,on_delete=models.SET_NULL , null=True )
    conversation_id_str = models.CharField(verbose_name="ID", max_length=50)
    favorite_count = models.IntegerField(verbose_name="Likes Count")
    reply_count = models.IntegerField(verbose_name="Replies Count")
    retweet_count = models.IntegerField(verbose_name="Retweet Count")
    user_id_str = models.CharField(verbose_name="User ID", max_length=50)
    bookmark_count =  models.IntegerField(verbose_name="BookMarked Count")
    media_links = models.ManyToManyField(MediaLink , blank=True )
    full_text = models.TextField(verbose_name="Body")
    quoted_retweted_from = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True,related_name="quotedretwetedfrom")
    retweted_from = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True,related_name="retwetedfrom")
    created_at = models.DateTimeField(verbose_name="Created At")
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.created_at.date()} - {self.conversation_id_str} {self.getString()}"

    def getString(self):
        string = ""
        if self.quoted_retweted_from :
            string += f'- Quoted Retweet {self.quoted_retweted_from.conversation_id_str}'
        elif self.retweted_from :
            string += f'- Retweet {self.retweted_from.conversation_id_str}'
        return string

    class Meta:
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

class Reply(models.Model):
    account = models.ForeignKey(TwitterAccount,on_delete=models.SET_NULL , null=True )
    conversation_id_str = models.CharField(verbose_name="ID", max_length=50)
    favorite_count = models.IntegerField(verbose_name="Likes Count")
    reply_count = models.IntegerField(verbose_name="Replies Count")
    retweet_count = models.IntegerField(verbose_name="Retweet Count")
    user_id_str = models.CharField(verbose_name="User ID", max_length=50)
    bookmark_count =  models.IntegerField(verbose_name="BookMarked Count")
    media_links = models.ManyToManyField(MediaLink , blank=True  )
    full_text = models.TextField(verbose_name="Body")
    media_url = models.CharField(verbose_name="Media URL", max_length=200)
    replied_from = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True,related_name="repliedfrom")
    in_reply_to_screen_name = models.CharField(verbose_name="Replying to", max_length=50,null=True)
    created_at = models.DateTimeField(verbose_name="Created At")
    created_datetime = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_datetime = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self) -> str:
        return f"{self.created_at.date()} - {self.conversation_id_str} {self.getString()}"

    def getString(self):
        string = ""
        if self.replied_from :
            string += f'- Replied To  {self.replied_from.conversation_id_str}'
        return string

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'


