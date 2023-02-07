from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact, Order, OrdersUpdate
from math import ceil
import datetime
import json

# Create your views here.
def index(request):
    # productname = Product.objects.all()
    # n = len(productname)
    # nslides = n//4 + ceil(n/4-n//4)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil(n/4-n//4)
        allProds.append([prod, range(1, nslides), nslides])

    # params = {"no_slides":nslides, "productname":productname, "range":range(1, nslides)}
    # allProds = [[productname, range(1,  nslides), len(productname)],
    #             [productname, range(1,  nslides), len(productname)]]

    params = {"allProds":allProds}
    return render(request, "shhop/main.html", params)

def searchitem(query, item):
    if query.lower() in item.product_name.lower() or query.lower() in item.desc.lower() or query.lower() in item.category.lower() or query.lower() in item.subcategory.lower():
        return True

    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchitem(query, item)]
        n = len(prod)
        nslides = n//4 + ceil(n/4-n//4)
        if len(prod) != 0:
            allProds.append([prod, range(1, nslides), nslides])
    params = {"allProds":allProds, "msg":""}

    if len(allProds) == 0 or len(query) < 4:
        params = {"msg":"we are sorry."}

    return render(request, "shhop/search.html", params)

def about(request):
    return render(request, "shhop/about.html")

def contact(request):
    thank=False
    if request.method == "POST":
        Nmae = request.POST.get('name', '')
        Email = request.POST.get('email', '')
        Phone = request.POST.get('phone', '')
        Desc = request.POST.get('desc', '')
        # print(Nmae)
        date_time = datetime.datetime.now()
        con = Contact(name=Nmae, email=Email, phone=Phone, desc=Desc, date=date_time)
        con.save()
        thank=True
    return render(request, "shhop/contact.html", {"thank":thank})

def tracker(request):
    if request.method == "POST":
        orderidn = request.POST.get('orderidn', '')
        Email__ = request.POST.get('Email__', '')
        # return HttpResponse(f"{orderidn} and {Email__}")
        try:
            # return HttpResponse(f"{orderidn} and {Email__}")
            order = Order.objects.filter(oder_id=orderidn, email_id=Email__)
            if len(order)>0:
                update = OrdersUpdate.objects.filter(orderid=orderidn)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    return render(request, "shhop/tracker.html")

def productView(request, myid):
    # Fetch the product using id
    prod = Product.objects.filter(id=myid)
    print(prod)
    return render(request, "shhop/productView.html", {'product':prod[0]})

def checkout(request):
    if request.method == "POST":
        item_jso = request.POST.get('itemsJson', ' ')
        Name = request.POST.get('name', '')
        email_ = request.POST.get('email2', '')
        add1 = request.POST.get('addr1', '')+", "+request.POST.get('addr2', '')
        phone_no = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_c = request.POST.get('zipt', '')
        date_tim = datetime.datetime.now()
        orde = Order(name=Name, email_id=email_, address=add1, phone=phone_no, city=city, state=state, zip_code=zip_c, items_json=item_jso, date_of_order=date_tim)
        orde.save()
        update = OrdersUpdate(orderid=orde.oder_id, update_desc="The order has been placed.")
        update.save()
        thank = True
        id = orde.oder_id
        return render(request, "shhop/checkout.html", {'thank':thank, 'id': id})
    return render(request, "shhop/checkout.html")