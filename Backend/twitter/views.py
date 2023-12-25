from rest_framework.response import Response 
from rest_framework.status import (
    HTTP_424_FAILED_DEPENDENCY,
    HTTP_400_BAD_REQUEST ,
    HTTP_200_OK ,
    HTTP_404_NOT_FOUND
    )
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from .models import Project , Agent 
from .serializer import ProjectSerializer , AgentSerializer
# from .TWlogin import LoginUsingBrowser
# from core.session import TwitterSession
# import datetime
# Create your views here.



class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AgentListView(ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer



@api_view(["POST"])
def checkExistAccountFBViews(request:Request):
    agentName = request.data.get('agentName','')
    if agentName :
        try : 
            agent = Agent.objects.get(name=agentName)
            return Response(
                AgentSerializer(agent).data ,
                status= HTTP_200_OK
            )
        except Agent.DoesNotExist :
            return Response(
                {} ,
                status= HTTP_404_NOT_FOUND
            )
    else :
        return Response(
            {"error":'"agentName" argument not found in request'} ,
            status = HTTP_400_BAD_REQUEST
            )



# @api_view(["POST"])
# def testLogin(request:Request):
#     login = request.data.copy()
#     print(login)
#     if login :
#         s = TwitterSession(login.get("cookie",""))
#         me = s.getMe()
#         print(me)
#         tt = s.getMyTweets(_from=datetime.datetime(2023,11,14))
#         return Response({'length':len(tt),'data':tt}) 
#     else :
#         return Response({},status=HTTP_424_FAILED_DEPENDENCY)

