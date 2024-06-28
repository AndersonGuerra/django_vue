from inertia import inertia

@inertia("home")
def home(request):
    return {
        'msg': 'Olá'
    }


@inertia("subpage/index")
def subpage(request):
    return {
        'msg': 'subpage'
    }