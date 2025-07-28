from itertools import product

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product,Category
from . import tasks
from django.contrib import messages
from utils import IsAdminUserMixin
from orders.forms import CartAddform
import random

# Create your views here.

class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories= Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)

        return render(request, 'home/home.html', {'products': products, 'categories':categories})

class GetAllCategoriesView(View):
    def get(self, request, slug=None):
        categories = Category.objects.filter(is_sub=False).prefetch_related('scategory')
        products = Product.objects.all()
        selected_category = None

        if slug:
            selected_category = get_object_or_404(Category, slug=slug)
            products = products.filter(category=selected_category)

        return render(request, 'home/all_category.html', {
            'categories': categories,
            'products': products,
            'selected_category': selected_category,
        })




class ProductDetailView(View):
    def get(self, request,product_id ,slug):
        product = get_object_or_404(Product,id=product_id , slug=slug)

        current_product_categories = product.category.all()
        print("Categories for current product:", [c.name for c in current_product_categories])

        related_books_queryset = Product.objects.filter(category__in=current_product_categories
                                                        ).exclude(id=product.id
                                                                  ).distinct()

        if related_books_queryset.count() > 4:
            related_books = random.sample(list(related_books_queryset), 4)
        else:
            related_books = list(related_books_queryset)

        print("Related Books Count:", len(related_books))  # این خط رو اضافه کنین
        for book in related_books:  # این حلقه رو هم اضافه کنین
            print("Related Book Name:", book.name)

        context = {
            'product': product,
            'related_books': related_books,
            'form': CartAddform(),
        }
        return render(request, 'home/detail.html', context)




class BucketHome(IsAdminUserMixin, View):
    template_name = 'home/bucket.html'
    def get(self, request):
        objects = tasks.all_bucket_objects_task()
        print(objects)
        return render(request, self.template_name, {'objects': objects})


class DeleteBucketObject(IsAdminUserMixin,View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request,'your object delete soon.','info')
        return redirect('home:bucket')

class DownloadBucketObject(IsAdminUserMixin,View):
    def get(self, request, key):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your download will start soon.', 'info')
        return redirect('home:bucket')










