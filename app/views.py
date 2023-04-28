from django.shortcuts import render

# Create your views here.
def Built_in_Filters(request):
    import datetime
    d={'data':'sHiVarAmRaj is A gOOd Boy','age':24,'gender':'MALE','date':datetime.datetime.now(),'c':2}
    return render(request,'Built_in_Filters.html',d)