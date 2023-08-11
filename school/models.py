from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    subject = models.CharField(max_length=64, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учителя'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    mentors = models.ManyToManyField(Teacher, through='StudentTeachers')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

    def __str__(self):
        return self.name


class StudentTeachers(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teachers', verbose_name="студент")
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teachers', verbose_name='учитель')

    class Meta:
        verbose_name = 'Учитель студента'
        verbose_name_plural = 'Учителя студентов'
