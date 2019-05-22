# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.safestring import mark_safe

from pages.models import PageTranslation, Page
from django.template.defaultfilters import truncatewords
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import admin
from django.urls import reverse, resolve


def get_title(obj):
    return truncatewords(obj.get_translation().title, 10)
get_title.short_description = "English Title"


def get_subject(obj):
    return truncatewords(obj.get_translation().subject, 10)
get_subject.short_description = "English Subject"


class PageTextAdmin(admin.ModelAdmin):
    model = PageTranslation
    list_display = ["model", "slug", "language"]
    readonly_fields = ["model", "language"]
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('model', "language")
        }),
        ("Details", {
            'fields': ('title', 'subtitle','slug')
        }),
        ("Content", {
            'fields': ('content', )
        }),
        ("SEO", {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_keywords',"meta_description")
        }),
    )

    def get_model_perms(self, request):
        return {}

    def changelist_view(self, request, extra_context=None):
        return HttpResponseRedirect(reverse("admin:snuza_page_changelist"))

admin.site.register(PageTranslation, PageTextAdmin)


class PageInline(admin.StackedInline):
    model = PageTranslation
    extra = 1
    max_num = 1
    aws_trans = None
    can_delete = False
    readonly_fields = ["language"]
    fieldsets = (
        (None, {
            'fields': ('language',("title", "subtitle",), "slug", "content")
        }),
        ("SEO", {
            'classes': ('collapse',),
            'fields': (('meta_title', 'meta_keywords',"meta_description",),)
        }),
    )

    def get_parent_object_from_request(self, request):
        resolved = resolve(request.path_info)
        if resolved.kwargs:
            return self.parent_model.objects.get(pk=resolved.kwargs["object_id"])
        return None

    def get_queryset(self, request):
        qs = super(PageInline, self).get_queryset(request)
        language = request.GET.get("language", "en")
        in_lang = False
        for lang in settings.LANGUAGES:
            if lang[0] == language:
                in_lang = True

        if in_lang:
            page = self.get_parent_object_from_request(request)
            try:
                en = PageTranslation.objects.get(model = page, language = "en")
                PageTranslation.objects.get_or_create(
                    model = self.get_parent_object_from_request(request),
                    language=language,
                    defaults = {
                        "title": en.title,
                        "slug": en.slug,
                        "subtitle": en.subtitle,
                        "content": en.content,
                    })
                qs = qs.filter(language=language)
            except:
                pass
        return qs

    def get_formset(self, request, obj=None, **kwargs):
        return super(PageInline, self).get_formset(request, obj, **kwargs)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'language':
            kwargs['initial'] = "en"
        return super(PageInline, self).formfield_for_dbfield(db_field, **kwargs)


def page_controls(obj):
    html = '<div style="width:340px;height:25px; line-height: 25px">'
    for lang in settings.LANGUAGES:
        html += '<a style="margin:5px" href="/admin/pages/page/%s/change/?language=%s" title="%s">' \
                '<img src="/static/img/flags/icons/%s.png"/></a>' % (obj.id, lang[0], lang[1].title(), lang[0])
    html += "</div>"
    return mark_safe(html)
page_controls.short_description = 'Controls'
page_controls.allow_tags = True


class PageAdmin(admin.ModelAdmin):
    search_fields = ["name", "slug"]
    list_display = ('name', get_title, 'slug', 'status', 'display', page_controls,)
    list_editable = ('display',)
    list_filter = ('display','status',)
    inlines = [PageInline,]
    prepopulated_fields = {'slug': ('name',)}
    change_form_template = "admin/pages_changeform.html"

    def response_change(self, request, obj):
        new_url = "%s?language=%s" % (reverse("admin:pages_page_change", args=(obj.pk,)), request.GET.get("language", "en"))
        return HttpResponseRedirect(new_url)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = {
            "set_lang": request.GET.get("language", "en")
        }
        return super(PageAdmin, self).change_view(request, object_id, form_url, extra_context)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.language:
                instance.language = "en"
            instance.save()
        formset.save_m2m()

    class Media:
        js = ("/static/js/jquery.min.js", "/static/js/admin_pages.js",
            "/static/js/tinymce/tinymce.min.js", "/static/js/tinymce.js",)

admin.site.register(Page, PageAdmin)

