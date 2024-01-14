from urllib.parse import unquote
from http.cookies import re, SimpleCookie
from .constants import TOKEN_IDENTIFIRE , USERID_IDENTIFIRE



class CookiesParser(object):
    def __init__(self,cookies) -> None:
        self.simplecookie = SimpleCookie()
        self.simplecookie.load(cookies)
        self.cookies_as_dict = {k: v.value for k, v in self.simplecookie.items()}

    @property
    def token(self):
        return unquote(self.cookies_as_dict[TOKEN_IDENTIFIRE])
    @property
    def userID(self):
        return unquote(self.cookies_as_dict[USERID_IDENTIFIRE]).split("=")[-1]


# def save(model,obj):
#     instance = model.objects.create(
#         **obj.data
#     )
#     instance.save()

# def check_date_range(datetime_list, from_date, to_date):
#     """
#     Check if each datetime object's date in the list falls within the specified date range.

#     Parameters:
#     - datetime_list (list): List of datetime objects to be checked.
#     - from_date (date): Start of the date range.
#     - to_date (date): End of the date range.

#     Returns:
#     - list: A list of boolean values indicating whether each datetime object's date is in the range.
#     """
#     result = [from_date <= dt.date() <= to_date for dt in datetime_list]
#     return result
