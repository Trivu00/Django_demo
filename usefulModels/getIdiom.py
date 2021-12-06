from .models import idiom4Day
from random import seed, randint
def getIdiom():
    id4idiom = randint(1, idiom4Day.objects.count())
    return idiom4Day.objects.get(pk=id4idiom)
    