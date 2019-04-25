import json

from django.shortcuts import render, redirect, HttpResponse
from index import models


# Create your views here.

def index(request):
    page_num = request.GET.get('page_num')
    if not page_num:
        page_num = 1
    all_book = models.Book.objects.all()
    all_publisher = models.Publisher.objects.all()
    all_author = models.Author.objects.all()
    return render(request, 'index.html',
                  {"all_publisher": all_publisher, 'all_book': all_book, 'all_author': all_author, 'page_num': page_num})


def add_publisher(request):
    all_author = models.Author.objects.all()
    all_publisher = models.Publisher.objects.all()
    if request.method == "POST":
        publisher_name = request.POST.get('publisher')
        models.Publisher.objects.create(name=publisher_name)
        return redirect('/')
    return render(request, 'add_publisher.html', {"all_publisher": all_publisher, 'all_author': all_author})





def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.getlist('author')
        publisher = request.POST.get('publisher')
        new_book_obj = models.Book.objects.create(title=title, publisher_id=publisher)
        new_book_obj.author.set(author)
        return redirect('/?page_num=2')


def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        models.Author.objects.create(name=author_name)
        return redirect('/?page_num=3')


def update_publisher(request):
    if request.method == "POST":
        publisher_id = request.POST.get('id')
        old_publisher = models.Publisher.objects.get(id=publisher_id)
        name = request.POST.get('publisher')
        old_publisher.name = name
        old_publisher.save()
        return redirect('/')
    # return render(request, 'update_publisher.html', {'old_publisher': old_publisher})


def update_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('id')
        # print(book_id)
        title = request.POST.get('title')
        author_list = request.POST.getlist('author')
        publisher = request.POST.get('publisher')
        old_book = models.Book.objects.get(id=book_id)
        old_author = models.Author.objects.filter(id__in=author_list)
        old_book.title = title
        old_book.publisher_id = publisher
        old_book.author.set(old_author)
        old_book.save()
        return redirect('/?page_num=2')


def update_author(request):
    if request.method == 'POST':
        author_id = request.POST.get('id')
        author_name = request.POST.get('author_name')
        old_author = models.Author.objects.get(id=author_id)
        old_author.name = author_name
        old_author.save()
        return redirect('/?page_num=3')


def delete_publisher(request):
    if request.method == "GET":
        publisher_id = request.GET.get('id')
        models.Publisher.objects.get(id=publisher_id).delete()
        return redirect('/')
    elif request.method == "POST":
        publisher_id = request.POST.get('id')
        book_obj = models.Book.objects.all().filter(publisher_id=publisher_id)
        title_list = []
        for book in book_obj:
            title_list.append(book.title)
        return HttpResponse(json.dumps(title_list), content_type="application/json")

def delete_book(request):
    book_id = request.GET.get('id')
    models.Book.objects.get(id=book_id).delete()
    return redirect('/?page_num=2')


def delete_author(request):
    if request.method == "GET":
        author_id = request.GET.get('id')
        models.Author.objects.get(id=author_id).delete()
        return redirect('/?page_num=3')
    elif request.method == "POST":
        author_id = request.POST.get('id')
        book_obj = models.Book.objects.all().filter(author=author_id)
        title_list = []
        for book in book_obj:
            title_list.append(book.title)
        return HttpResponse(json.dumps(title_list), content_type="application/json")


def test(request):
    author_id = 3
    book_obj = models.Book.objects.all().filter(author=author_id)
    title_list = []
    for book in book_obj:
        print(book.title)
    return HttpResponse('ok')