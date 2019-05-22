from django.core.management import BaseCommand, call_command
from django.conf import settings
from pages.functions import mkdir_p
import polib

class Command(BaseCommand):
    def handle(self, *args, **options):
        mkdir_p("%s/webapp/locale/" % settings.BASE_DIR)

        call_command('makemessages', "-l", "en", verbosity=0, interactive=False)
        po = polib.pofile("%s/webapp/locale/en/LC_MESSAGES/django.po" % (settings.BASE_DIR))
        for entry in po:
            if not entry.msgctxt or entry.msgctxt.replace(" ", "") == "":
                print(entry.msgctxt)
                print(entry.msgid)
                print("----------------------")
