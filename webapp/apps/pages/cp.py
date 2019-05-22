import datetime
from django.utils.translation import activate
from django.conf import settings

from pages.models import Page


def global_settings(request):
    context = {}
    context["TIMESTAMP"] = datetime.datetime.now()

    if request.GET.get("lang",False):
        in_lang = False
        lang = request.GET["lang"]
        for ilang in settings.LANGUAGES:
            if ilang[0] == lang:
                in_lang = True
        if in_lang:
            request.session["language"] = request.GET.get("lang", request.session.get("language", "en"))

    if not request.session.get("language", False):
        request.session["language"] = "en"

    has_page_perm = False
    if request.user.is_authenticated:
        if "/admin/" in request.path:
            request.session["language"] = "en"
        for perm in request.user.get_all_permissions():
            if "pages." in perm:
                has_page_perm = True

    activate(request.session["language"])
    request.session.modified = True
    context["VERSION"] = settings.VERSION
    context["SET_LANG"] = request.session["language"]
    context["PAGE_LIST"] = Page.objects.filter(display=True)
    return context