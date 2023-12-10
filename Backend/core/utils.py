from urllib.parse import unquote

TOKEN_IDENTIFIRE = "ct0" 
ID_IDENTIFIRE = "twid"

def getValuesFromCookie(identifire:str, cookie:str)->dict:
    value = ''
    key = identifire
    for slice in cookie.split(";") :
        if identifire in slice :
            key , value = slice.split("=")
            break
    return {key.replace(" ",""):unquote(value).replace(" ","")}
     

def getToken(cookie:str)->str:
    return getValuesFromCookie(TOKEN_IDENTIFIRE,cookie)[TOKEN_IDENTIFIRE]

def getUserID(cookie:str)->str:
    user_id:str = getValuesFromCookie(ID_IDENTIFIRE,cookie)[ID_IDENTIFIRE]
    return user_id.split("=")[-1]


