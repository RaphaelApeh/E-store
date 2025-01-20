import datetime


def show_year(request):

    return {
        "year": datetime.datetime.now().year
    }