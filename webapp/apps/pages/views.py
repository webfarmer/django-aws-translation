import simplejson

from pages.models import Page, PageTranslation
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse, Http404
from django.template import loader
import boto3

class HomeView(TemplateView):
    template_name = "pages/home.html"

class PageView(DetailView):
    template_name = "pages/page.html"
    model = Page
    context_object_name = "page"

    def get_object(self, queryset=None):
        try:
            return Page.objects.get(slug=self.kwargs["slug"])
        except:
            try:
                return PageTranslation.objects.get(slug=self.kwargs["slug"]).model
            except:
                raise Http404()


def fail_render(request, template_name):
    context = {}
    t = loader.get_template(template_name=template_name)
    return HttpResponse(t.render(context, request))


def handler400(request, template_name='400.html'):
    return fail_render(request, template_name=template_name)

def handler404(request, template_name='404.html'):
    return fail_render(request, template_name=template_name)

def handler403(request, template_name='403.html'):
    return fail_render(request, template_name=template_name)

def handler500(request, template_name='500.html'):
    return fail_render(request, template_name=template_name)


def FailView(request, slug):
    if slug == "400":
        return handler400(request)
    if slug == "403":
        return handler403(request)
    if slug == "500":
        return handler500(request)
    return handler404(request)


def AdminTranslateView(request):
    aws_access_key_id = "AKIAI3PONSWZQPXMTVVA"
    aws_secret_access_key = "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"
    aws_region = "us-east-1"

    aws = boto3.client('translate',
                       aws_access_key_id=aws_access_key_id,
                       aws_secret_access_key=aws_secret_access_key,
                       region_name=aws_region)

    response = {"status": False}

    if request.POST.get("text", False):
        res = aws.translate_text(
            Text=request.POST["text"],
            SourceLanguageCode="en",
            TargetLanguageCode=request.POST["language"]
        )
        response = {
            "status": True,
            "translated": res["TranslatedText"]
        }


    return HttpResponse(simplejson.dumps(response), content_type="application/json")
