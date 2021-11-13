from django import forms
from django.forms import fields

from .models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ["title", "content"]

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Articles.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already in use.")

        return data


class ArticleFormold(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data  # dict
    #     print("cleaned_data", cleaned_data)
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("this title is already taken")

    # print("title", title)
    # return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print("all data", cleaned_data)
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "the office":
            self.add_error("title", "this title is already taken")
            # raise forms.ValidationError("this title is already taken")

        if "office" in content.lower().strip() or "office" in title.lower().strip():
            self.add_error("content", "office cannot be in content")
            raise forms.ValidationError("office is not allowed")

        return cleaned_data
