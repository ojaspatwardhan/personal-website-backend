from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import ProjectSerializer, HobbySerializer
from .models import Project, Hobby
from django.core.mail import send_mail


# Create your views here.

class WebsiteView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    @action(detail=False, methods=['post'], url_path="send-email")
    def send_email(self, email):
        sender = email
        print(sender)
        send_mail(
            subject="Test email",
            message="This is an automated reply. Please don't reply to this email.",
            from_email=str(sender),
            recipient_list=["ojas.patwardhan@gmail.com"],
            fail_silently=False
        )
        return HttpResponse('success')


class HobbyView(viewsets.ModelViewSet):
    serializer_class = HobbySerializer
    queryset = Hobby.objects.all()
