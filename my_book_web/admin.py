from django.contrib import admin

# Register your models here.
from my_book_web.models import Books, Author, Genre

@admin.register(Books)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GradeAdmin(admin.ModelAdmin):
    pass