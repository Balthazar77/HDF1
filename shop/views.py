from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category, Product, Brand
from cart.forms import CartAddProductForm


class ProductListView(ListView):
    """Запрос ко БД ко всем полям """
    template_name = 'shop/base.html'
    context_object_name = 'product'
    model = Product

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        return queryset.filter().all()[:10]

    """Функция запроса к БД для дополнительного отбражение катагория"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    brand = Brand.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'brand': brand
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})