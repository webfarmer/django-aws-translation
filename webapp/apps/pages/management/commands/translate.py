import boto3
from django.core.management import BaseCommand, call_command
from django.conf import settings
import polib, sys

from pages.functions import mkdir_p

class Command(BaseCommand):
    aws_access_key_id = "AKIAI3PONSWZQPXMTVVA"
    aws_secret_access_key = "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"
    aws_region = "us-east-1"

    def handle(self, *args, **options):
        mkdir_p("%s/webapp/locale/" % settings.BASE_DIR)

        aws_trans = boto3.client('translate',
                            aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key,
                            region_name=self.aws_region)

        lang_list = settings.LANGUAGES

        for li, lang in enumerate(lang_list):
            call_command('makemessages', "-l", lang[0], verbosity=0)
            po = polib.pofile("%s/webapp/locale/%s/LC_MESSAGES/django.po" % (settings.BASE_DIR, lang[0]))
            if li:
                print("\n ---------------------------------------------------------------------------------- ")
                print("     Translating %s" % lang[1]),
            else:
                print(" ---------------------------------------------------------------------------------- ")
                print("                            AWS TRANSLATION TOOL")
                print(" ---------------------------------------------------------------------------------- ")
                print("    We are about to translate the connect webapp into the following languages:")
                print("    ", end="")
                for ilang, llang in enumerate(lang_list):
                    print (llang[1], end="")
                    if ilang != len(lang_list) - 1:
                        print(",", end=" ")
                    else:
                        print("", end="")
                print("")
                print(" ---------------------------------------------------------------------------------- ")
                print("     Translating %s" % lang[1])

            icount = len(po)
            for m, entry in enumerate(po):
                percentage = (m + 1) * 100 / icount
                p = percentage * 30 / 100
                eq = self.repeat_to_length("=", int(p))
                blank = self.repeat_to_length("_", int(30 - p))

                response = aws_trans.translate_text(Text=entry.msgid,
                                                    SourceLanguageCode="en",
                                                    TargetLanguageCode=lang[0])
                entry.msgstr = response["TranslatedText"]

                sys.stdout.write(("\r     %d of %d words/phrases [" + str(eq) + str(blank) + "] %d%%  ") % ((m + 1), icount, percentage))
                sys.stdout.flush()
                
            po.save()
            po.save_as_mofile("%s/webapp/locale/%s/LC_MESSAGES/django.mo" % (settings.BASE_DIR, lang[0]))

        print("\n ---------------------------------------------------------------------------------- ")
        print("    Complete! Have a great Day :)")
        print(" ---------------------------------------------------------------------------------- ")

    def repeat_to_length(obj, string_to_expand, length):
        return (string_to_expand * (int(length / len(string_to_expand)) + 1))[:length]