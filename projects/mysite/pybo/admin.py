from django.contrib import admin

from .models import Question

# Register your models here.
# 모델들을 Admin에 등록하면 손쉽게 모델을 관리 가능 
# 쉘에서 수행했던 데이터 저장, 수정, 삭제 등의 작엄들을 장고 Admin에서 할 수 있다.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']



admin.site.register(Question, QuestionAdmin)