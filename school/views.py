from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


class StudentsList(ListView):
    template_name = 'school/students_list.html'
    model = Student

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        ordering = 'group'
        students = Student.objects.prefetch_related('teachers').order_by(ordering)
        context = {'object_list': students}

        return context

        # return render(request, template, context)
