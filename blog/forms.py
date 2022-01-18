from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=75,
        label="Name",
        widget=forms.TextInput(attrs={"placeholder": "Name"}),
    )
    email = forms.EmailField(
        label="Email from", widget=forms.EmailInput(attrs={"placeholder": "Email from"})
    )
    to = forms.EmailField(
        label="Email to", widget=forms.EmailInput(attrs={"placeholder": "Email to"})
    )
    comments = forms.CharField(
        required=False,
        label="Comments",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Comments"}),
    )


class CommentForm(forms.ModelForm):
    name = forms.CharField(
        label="Name", widget=forms.TextInput(attrs={"placeholder": " Name"})
    )
    email = forms.CharField(
        max_length=254,
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": " Email"}),
    )
    body = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Message"}),
    )

    class Meta:
        model = Comment
        fields = ("name", "email", "body")


class SearchForm(forms.Form):
    query = forms.CharField(
        label="Search", widget=forms.TextInput(attrs={"placeholder": "post"})
    )
