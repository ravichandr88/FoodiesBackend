from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets




from .models import Food
from .models import Meal
from .models import BEVERAGES
from .models import COMBOS
from .models import Slider
from .models import Gallery
# from .serializers import MealPicSerializer
from .serializers import MealSerializer

from .serializers import FoodSerializer
from .serializers import BEVERAGESSerializer
from .serializers import COMBOSSerializer
from .serializers import SliderSerializer
from .serializers import GallerySerializer













from django.contrib.auth import get_user_model, login, logout # new
from django.contrib.auth.forms import AuthenticationForm # new
from rest_framework import generics, permissions, status, views # new
from rest_framework.response import Response

from .serializers import UserSerializer



from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect






#contact form send email

from rest_framework import viewsets
from .models import Consult
from .serializers import ConsultSerializer
from django.core.mail import EmailMessage

from django.core.mail import send_mail


from django.core import serializers

# data = serializers.serialize("xml", Consult.objects.all())

# def send_email():
#     email = EmailMessage(
#         'SEND',
#         (ConsultSerializer.name, ConsultSerializer.subject, ConsultSerializer.message),
#         'my-email',
#         ['ak080495@gmail.com']
#     )
#     # email.attach_file(ConsultSerializer.file)
#     email.send()





class ConsultViewSet(viewsets.ModelViewSet):
    
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer


    def create(self, request, *args, **kwargs):
        response = super(ConsultViewSet, self).create(request, *args, **kwargs)
        send_email(request)  # sending mail
        return response













 
    # def create(self, request, *args, **kwargs):
    #     response = super(ConsultViewSet, self).create(request, *args, **kwargs)

    #     subject = 'this is contact message' 
      
    #     message = request.POST.get('message', '')
    #     email = request.POST.get('username', '')
    #     recipient_list = [request.POST.get('email', ''),'ak080495@gmail.com','arunsamal4@gmail.com '] 
    #      '
    #     send_mail(subject, message, email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)  # sending mail
    #     return response 







    # def create(self, request, *args, **kwargs):
    #     response = super(ConsultViewSet, self).create(request, *args, **kwargs)
    #     # auth_user = request.POST.get('name', '')
    #     subject = request.POST.get('subject', '')
    #     message = request.POST.get('message', '')
    #     from_email = request.POST.get('name', '')

    #     recipient_list = [request.POST.get('from_email', ''),'ak080495@gmail.com']

    #     # ,request.POST.get('from_email', '')

    #     # subject = 'Thank you for registering to our site' static subject
    #     # message = ' it  means a world to us '
    #     # from_email = request.POST.get('from_email', '') user email
    #     # recipient_list = ['ak080495@gmail.com'] send only given one
    #     # recipient_list = [request.POST.get('from_email', ''),'ak080495@gmail.com']  to send user also
    #     # 'arunsamal4@gmail.com '
    #     send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)  # sending mail
    #     return response 






def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['ak080495@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')  









    # def create(self, validate_data):
    #     instance = super(ConsultViewSet, self).create(validate_data)
    #     send_mail(
    #         'Instance {} has been created'.format(instance.name),
    #         'Here is the message. DATA: {}'.format(validate_data),
    #         'from@example.com',
    #         ['to@example.com'],
    #         fail_silently=False,
    #     )
    #     return instanc


    # def create(self, request, *args, **kwargs):
    #     response = super(ConsultViewSet, self).create(request, *args, **kwargs)
    #     serailizer = ConsultSerializer(request.data)
    #     if serailizer.is_valid(self):
    #          data = serailizer.validated_data
    #          email = validated_data.get('email')
    #          name = validated_data.get('name')
    #          send_mail(
    #             'Sent email from {}'.format(name),
    #             'Here is the message. {}'.format(validate_data.get('message')),
    #             email,
    #             ['to@example.com'],
    #             fail_silently=False,
    #         )
    #     return response({"success": "Sent"})
    #     return response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)












    # def create(self, request, *args, **kwargs):
    #     response = super(ConsultViewSet, self).create(request, *args, **kwargs)


    #     subject = 'Thank you for registering to our site'
    #     message = ' it  means a world to us '
    #     send_mail('Account created', 'welcome to foodiesplace.', 'from@example.com', ['ak080495@gmail.com'], fail_silently=False,)  # sending mail
    #     return response 


# def send_email():
#     email = EmailMessage(
#         'Title',
#         str(ConsultSerializer.name, ConsultSerializer.email, ConsultSerializer.phone),
#         'my-email',
#         ['my-receive-email']
#     )
#     email.attach_file(ConsultSerializer.file)
#     email.send()





class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer  #for html form





    def create(self, request, *args, **kwargs):
        response = super(SignUpView, self).create(request, *args, **kwargs)

        subject = 'Thank you for registering to our site' 
        # static subject
        message = ' it  means a world to us '
        email = request.POST.get('username', '')
        recipient_list = [request.POST.get('email', ''),'ak080495@gmail.com','arunsamal4@gmail.com '] 
        # send only given one
        # recipient_list = [request.POST.get('from_email', ''),'ak080495@gmail.com']  to send user also
        # 'arunsamal4@gmail.com '
        send_mail(subject, message, email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)  # sending mail
        return response 




class LogInView(views.APIView): # new
    def post(self, request):
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            login(request, user=form.get_user())
            return Response(UserSerializer(user).data)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(views.APIView): # new
   

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserList(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer




class UserDetail(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


    

class MealViewSet(viewsets.ModelViewSet):
    serializer_class = MealSerializer
    queryset = Meal.objects.all()

    
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
        partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()

    
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
        partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class BEVERAGESViewSet(viewsets.ModelViewSet):
    serializer_class = BEVERAGESSerializer
    queryset = BEVERAGES.objects.all()

    
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
        partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class COMBOSViewSet(viewsets.ModelViewSet):
    serializer_class = COMBOSSerializer
    queryset = COMBOS.objects.all()

    
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
        partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class SliderViewSet(viewsets.ModelViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()

    
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
        partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)



class  GalleryViewSet(viewsets.ModelViewSet):
    serializer_class =  GallerySerializer
    queryset =  Gallery.objects.all()

    
    def pic(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
        partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,status.HTTP_400_BAD_REQUEST)