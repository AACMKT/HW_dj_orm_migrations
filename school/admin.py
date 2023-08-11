from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Student, Teacher, StudentTeachers


class StudentTeachersInlineFormset(BaseInlineFormSet):
    def clean(self):
        names = []
        for form in self.forms:
            form.cleaned_data
            if form.cleaned_data.get('teacher_name') is not None:
                names.append(form.cleaned_data.get('teacher_name'))
        if len(names) == 0:
            raise ValidationError('Укажите минимум одного учителя')
        else:
            for name in names:
                if names.count(name) > 1:
                    raise ValidationError('Повторное указание того же учителя не допускается')

        return super().clean()


class StudentTeachersInline(admin.TabularInline):
    model = StudentTeachers
    formset = StudentTeachersInlineFormset
    # extra = 3


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    inlines = [StudentTeachersInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']


# @admin.register(StudentTeachers)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ['student_name', 'teacher_name']
