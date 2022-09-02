from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,HttpResponse

pathList = ["/login","/logout","/register","/uploadImage"]
# pathList = []

class AuthMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        return

        if request.path_info in pathList:
            return

        info_dict = request.session.get('info')
        if info_dict:
            return

        return redirect("/login")