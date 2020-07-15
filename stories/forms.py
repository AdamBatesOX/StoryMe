from django import forms

from .models import Story

import re

MAX_STORY_LENGTH = 100

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        #if len(content) > MAX_STORY_LENGTH:
        if len(re.findall(r'\w+', content)) > MAX_STORY_LENGTH: #line to set word limit 
            raise forms.ValidationError("This story is too long")
        return content