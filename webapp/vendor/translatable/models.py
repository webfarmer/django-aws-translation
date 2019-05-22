from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _, get_language
from django.core.exceptions import ObjectDoesNotExist
from vendor.translatable.exceptions import MissingTranslation

class TranslatableModel(models.Model):
    """
    Base class for translatable models. Its subclasses should contain only language-independent
    fields such as foreign keys.
    """
    translations = None

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.get_translation(), "utf-8")

    def has_translations(self):
        """
        Checks if this model has any translation available.
        """
        return self.translations.exists()

    def has_translation(self, language=None):
        """
        Returns model translation in a language having given `language` code. If no language code
        is given, current language of Django internationalization system is used.
        """
        language = language or get_language()
        return self.translations.filter(language=language).exists()

    def get_translation(self, language=None, fallback=True):
        """
        Returns model translation in a language having given `language` code. If no language code
        is given, current language of Django internationalization system.

        If `fallback` is True (default) first available translation is returned. Languages are
        check in order of `LANGUAGES` setting.

        If no translation was found in any of previous steps, `MissingTranslation` exception is
        raised.
        """
        language = language or get_language()
        try:
            return self.translations.get(language=language)
        except ObjectDoesNotExist:
            if fallback:
                for other_language, other_language_name in settings.LANGUAGES:
                    if other_language == language:
                        continue
                    try:
                        return self.translations.get(language=other_language)
                    except ObjectDoesNotExist:
                        continue
        raise MissingTranslation

    def translated(self, field_name, default=None, language=None, fallback=True):
        """
        Returns field of translation. Arguments `language` and `fallback` are
        same as passed to `get_translation` method. If `get_translation` raises
        `MissingTranslation` exception, `default` value is returned (None for default).
        """
        try:
            return getattr(self.get_translation(language=language, fallback=fallback), field_name)
        except MissingTranslation:
            return default

def get_translation_model(translatable_model, verbose_name):
    """
    Returns a base class for translation of given `translatable_model`. Attribute `verbose_name`
    is used for a foreign key connecting it to the model it translates.
    """
    class TranslationModel(models.Model):
        model = models.ForeignKey(translatable_model, on_delete=models.CASCADE, related_name='translations', verbose_name=verbose_name)
        language = models.CharField(_("language"), max_length=15, choices=settings.LANGUAGES)
        class Meta:
            abstract = True
        unique_together = (
            ('model', 'language'),
        )
    return TranslationModel

