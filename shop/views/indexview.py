from django.shortcuts import render

def my_view(request):
    
    context = {
        "products":[
        {"name":"Product 1","price":1.5},
        {"name":"Product 2","price":2.75},
        {"name":"Product 3","price":6},
    ]
    }
    return render(request, "shop/index.html", context)