from django.views.generic import TemplateView
import json
from os.path import join

with open(join("vue", "application.json"), "r", encoding="utf-8") as json_file:
    data = json.load(json_file)


class Index:
    @staticmethod
    def get(application_name):
        if application_name in data:
            return TemplateView.as_view(template_name=join(application_name, "index.html"))
        else:
            # TODO:改为404等页面,
            print("未注册该页面")
            return None
