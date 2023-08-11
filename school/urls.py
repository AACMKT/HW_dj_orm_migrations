from django.urls import path

from school.views import StudentsList

urlpatterns = [
    # path('', students_list, name='students'),
    path('', StudentsList.as_view(), name='students')

]
