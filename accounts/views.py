from djoser.views import UserViewSet
from djoser.compat import get_user_email
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from djoser.email import PasswordResetEmail
from .tasks import task_sender



class CustomUserView(UserViewSet):
    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user()

        if user:
            context = {"user": user}
            to = [get_user_email(user)]
            
            # Sending Reset Email Through Celery Task
            task_sender.delay(PasswordResetEmail(self.request,context).send(to))

            # settings.EMAIL.password_reset(self.request, context).send(to)

        return Response(status=status.HTTP_204_NO_CONTENT)