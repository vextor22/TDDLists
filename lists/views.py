from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError

from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(f'/lists/{list_.id}/')
        except ValidationError:
            error = "You can't have an empty list item"
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items, 'list_id': list_id, 'error': error})
#    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    item = Item(text=new_item_text, list=list_)
    try:
        item.full_clean()
        print(item.text)
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{list_.id}/')

