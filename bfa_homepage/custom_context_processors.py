import datetime

from django.conf import settings
from django.db.models import get_app, get_models

models = {m.__name__: m.objects for m in get_models(get_app("bfa_homepage"))}

def custom(request):
    return {
        "year": datetime.date.today().year,
        "models": models,
    }
