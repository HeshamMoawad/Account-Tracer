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
from ..models import (
    Project , 
    Agent , 
    AccountLoginInfo , 
    TwitterAccount ,
    Tweet ,
     )
from .serializer import (
    ProjectSerializer , 
    AgentSerializer , 
    AccountLoginInfoSerializer,
    AnalyticsSerializer ,
    TweetSerializer
    )
from ..core.session import TwitterSession
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime , timedelta
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

    def get(self,request:Request , *args , **kwargs):
        _filter = request.query_params.getlist("filter",None)
        if _filter :
            _filter = [arg for arg in _filter[0].split(",")]
            projects = Project.objects.filter(name__in=_filter).all()
            self.queryset = Agent.objects.filter(project__in=projects)
            return self.list(request ,*args,**kwargs)
        else :
            if isinstance(_filter,type(None)):
                return self.list(request ,*args,**kwargs)
            else :
                self.queryset = []
                return self.list(request ,*args,**kwargs)


class AccountLoginInfoListView(ListAPIView):
    queryset = AccountLoginInfo.objects.all()
    serializer_class = AccountLoginInfoSerializer

    def get(self , request:Request , *args , **kwargs):
        _project = request.query_params.get('project',None)
        _agent = request.query_params.get('agent',None)
        if _project and _agent :
            try : 
                project = Project.objects.get(name = _project)
                agent = Agent.objects.get(name = _agent , project = project)
                twitter_accounts = TwitterAccount.objects.filter(agent = agent).all()
                self.queryset = AccountLoginInfo.objects.filter(account__in=twitter_accounts).all()
            except ObjectDoesNotExist:
                self.queryset = []
            return self.list(request ,*args,**kwargs)
        else :
            self.queryset = []
            return self.list(request ,*args,**kwargs)



@api_view(["GET"])
def checkExistAccountFBViews(request:Request):
    agentName = request.query_params.get('agentName','')
    project_name = request.query_params.get('project','')
    if agentName and project_name:
        try : 
            project = Project.objects.get(name = project_name)
            agent = Agent.objects.get(name = agentName , project = project)
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


@api_view(["POST"])
def analyticsFBViews(request:Request):
    handle = request.data.get("handle",None)
    date = request.data.get("date",None)
    if handle :
        account = TwitterAccount.objects.filter(handle=handle).first()
        if account :
            logininfo = AccountLoginInfo.objects.get(account=account)
            analytics_serializer = AnalyticsSerializer(instance = logininfo)
            if date :
                date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(days=-1)
                analytics_serializer.set_conditions(created_datetime__date = date)
            return Response(
                analytics_serializer.data 
            )
        else : 
            return Response(
                {} ,
                status = HTTP_200_OK 
            )
    else :
        return Response(
            {"error":'"handle" param not found in request'} ,
            status = HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def checkExistHandleFBViews(request:Request):  # must uncomment maxDate in production
    handle = request.query_params.get("handle",None)
    try :
        account = AccountLoginInfo.objects.get(screen_name = handle)
        return Response(
            {
                "name" : account.name,
                "handle" : account.account.handle ,
                "profileImgURL" : account.profileImgURL ,
                "minDate" : account.created_datetime ,
                "maxDate" : datetime.now().date()
            } ,
        )
    except AccountLoginInfo.DoesNotExist :
        return Response(
            {} ,
            status = HTTP_404_NOT_FOUND
        )
    

@api_view(["GET"])
def testing(request:Request):
    account = AccountLoginInfo.objects.first()
    session = TwitterSession(account.cookies)
    session.saveMyStats()
    session.saveMyTweets()
    session.saveMyChats()


    return Response({})


class TweetListView(ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get(self,request:Request):
        date = datetime.strptime(request.query_params.get("date"), "%d/%m/%Y")
        screen_name = request.query_params.get("screen_name")
        account = AccountLoginInfo.objects.filter(screen_name=screen_name)
        if account.count() >= 1 :
            account = account.first()
            self.queryset = Tweet.objects.filter(account=account.account , created_at__date = date.date())
        else :
            self.queryset = []
        response =  self.list(request)
        response.data = {
            "data" : response.data ,
            "user" : {
                "profileImgURL" : account.profileImgURL ,
                "name" : account.name ,
            }
            }
        return response

