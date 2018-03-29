from django.contrib import admin

from .models import Question, Quiz, Answer


# class ChoiceInLine(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldssets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInLine]


class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # def __init__(self, *args, **kwargs):
    #     super(QuestionAdmin, self).__init__(*args, **kwargs)
    #     if self.instance.pk:
    #         categories = self.instance.category.all()
    #     else:
    #         categories = None
    #
    #     if categories:
    #         self.fields['topic'].queryset = self.fields['topic'].queryset.filter(category__in=categories)
    #     else:
    #         del self.fields['topic']
    #
    # class Meta:
    #     model = Question
    #     fields = [...]
    fieldsets = [
        (None, {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [AnswerInLine]

class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Quiz name', {'fields':['quiz_name']}),
    ]
    inlines = [QuestionInLine]
    
    
admin.site.register(Question,QuestionAdmin)
admin.site.register(Quiz,QuizAdmin)

