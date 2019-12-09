from django.http import HttpResponse
from django.shortcuts import render
import operator

def ram(request):
    return render(request,"Countwords.html")

def about(request):
    return render(request,"aboutus.html")

def count(request):
    mess=request.GET['message']
    wl=mess.split()
    wlcount = {}
    for words in wl:
        if words in wlcount:
            wlcount [words]+=1
        else:
            wlcount [words] =1
    sort1= sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True)
        # count[words]=count.get(words,0)+1
        # print(count)
    return render(request,"count.html", {"mess": mess,"length":len(wl),"abc":wlcount,'cba':sort1})
    # return render(request,"count.html",{"mess":mess,"length":len(wl)})
def pic(request):
    return HttpResponse("<h1> WELCOME TO ANIL KUMAR<h1>, <h2>ajdjjf,<h2>")

# def ram(request):
#     return HttpResponse("Hai anil Ganji")
