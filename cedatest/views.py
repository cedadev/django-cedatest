from django.http import HttpResponse
from cedatest_control.models import User

# Create your views here.

def list_users(request):
    users = User.objects.all()
    user_string = ""
    for user in users:
        user_string += ("{}\t\t: {}\n".format(user.name, user.email))
    return HttpResponse(user_string, content_type="text/plain")
