from django.utils.translation import pgettext
from pages.models import Newsletter
from django import forms

class NewsletterForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)

    def clean(self):
        if self.cleaned_data.get("email", False):
            if Newsletter.objects.filter(email = self.cleaned_data["email"]).count():
                self._errors["email"] = pgettext(u"msg_newsletter_email_exists",u"We already have this email in our system.")
        else:
            self._errors["email"] = pgettext(u"msg_email_exists",u"The email is required.")
        return self.cleaned_data


class MainCopyForm(forms.Form):
    page_slug = forms.SlugField()
    title = forms.CharField(widget=forms.Textarea)
    subtitle = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)


