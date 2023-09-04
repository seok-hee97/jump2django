from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)  # 제목은 최대 200자
    content = models.TextField()                # 내용
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    
    def __str__(self):
        return self.subject


#Answer 모델은  어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 함
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # 다른 모델의 속성으로 가지면 ForeignKey 이용
    # ForeignKey는 쉽게 말해 다른 모델과의 연결 의미, on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함꼐 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    #null=True는 데이터베이스에서 modify_date 칼럼에 null 허용
    #blank=True는 form.is_valid()를 통한 입력 데이터 검증 시 값이 없어도 됨
    #null=True, blank=True 는 어떤 조건으로든 값을 비워둘 수 있음
    voter = models.ManyToManyField(User, related_name='voter_answer')
    
    