from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if len(self.cleaned_data['title']) < 1 or len(self.cleaned_data['text']) < 1:
            raise forms.ValidationError("Title and text must be filled!")

    def save(self):
        question = Question.objects.create(**self.cleaned_data)
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    def clean(self):
        if len(self.cleaned_data['text']) < 1:
            raise forms.ValidationError("Text must be filled!")

    def save(self):
        try:
            question = Question.objects.get(pk=self.cleaned_data['question'])
        except Question.DoesNotExist:
                question = None
        answer = Answer.objects.create(
            text=self.cleaned_data['text'],
            question=question

        )
        return answer
