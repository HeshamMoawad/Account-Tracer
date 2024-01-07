
class User(object):
    def __init__(self, **kwargs):
        self.params_new_instance = {}
        self.params_new_instance.update({
            "rest_id" : kwargs.get("rest_id") ,
        })
        legacy:dict = kwargs["legacy"]
        self.params_new_instance.update({
            "name" : legacy.get("name","Can't Parse") ,
            "screen_name" : legacy.get("screen_name",f"{self.params_new_instance.get('rest_id')}") ,
            "description" : legacy.get("description"," "),
            "profileImgURL" : legacy.get("profile_image_url_https"," ") ,
            "verified" : bool(legacy.get("verified",False)) ,
            "suspend" : bool(legacy.get("suspended",False))  ,
            "created_at" : legacy.get("created_at","")
        })


    def __getitem__(self,__o:str):
        return self.params_new_instance.get(__o)
