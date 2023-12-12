from rest_framework.response import Response 
from rest_framework.status import HTTP_424_FAILED_DEPENDENCY
from rest_framework.request import Request
from rest_framework.decorators import api_view
 
from .TWlogin import LoginUsingBrowser
from core.session import TwitterSession
# Create your views here.

@api_view(["GET"])
def checkExistAccountFViews(request:Request):
    print(request)
    return Response({"hi":1})



@api_view(["POST"])
def testLogin(request:Request):
    # print(request.data)
    # print(type(request.data))
    # username = request.data.get("username",None)
    # password = request.data.get("password",None)
    # if not isinstance(username , type(None)) and not isinstance(password,type(None)) :
    #     loginobj = LoginUsingBrowser()
    #     login =  loginobj.login(username , password)
    # else :
    #     login = None
    login = request.data
    print(login)
    if login :
        s = TwitterSession(login.get("cookie",""))
        tt = s._getTweets()
        print(tt)
        return Response({'data':dict(tt)}) 
    else :
        return Response({},status=HTTP_424_FAILED_DEPENDENCY)

