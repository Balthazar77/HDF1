from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from organizations.models import DataUserOrganization
from organizations.views import Profile
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth import authenticate, login, get_user_model


# def order_create(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order,
#                                          product=item['product'],
#                                          price=item['price'],
#                                          quantity=item['quantity'])
#             # очистка корзины
#             cart.clear()
#             return render(request, 'orders/order/created.html',
#                           {'order': order})
#     else:
#         form = OrderCreateForm
#     return render(request, 'orders/order/create.html',
#                   {'cart': cart,  'form': form})

class Order(Profile):
    form_class = OrderCreateForm
    template_name = 'orders/order/create.html'

    def get(self, request, **kwargs):
            cart = Cart(request)
            # orders = DataUserOrganization.objects.filter(account=self.request.user).first()
            if request.method == 'POST':
                form = OrderCreateForm(request.POST)
                if form.is_valid():
                    # orders = self.initials
                    order = form.save()
                    for item in cart:
                            OrderItem.objects.create(order=order,
                                                     product=item['product'],
                                                     price=item['price'],
                                                     quantity=item['quantity'])
                            # очистка корзины
                    cart.clear()
                return render(request, 'orders/order/created.html',{'order': order})
            else:
                 # # form = self.form_class(initials=self.initials)
                 # return render(self.render_form(form))
                 form = self.form_class
                 return render(request, 'orders/order/create.html',
                               {'cart': cart, 'form': form})

    #         return self.render_form(form)
    #
    #
    # def render_form(self, form, *args, **kwargs):
    #     organizations = User.objects.filter(username=self.request.user)
    #     return render(self.request, self.template_name,
    #                       {'form': form, 'DataUserOrganization': organizations})