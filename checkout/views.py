from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PDqmrRqnOOoFJXg8xzj1cw33uEaHRTBst9gACOiHMEXRLEFnDYvkQ0camZUDOf5jzs6eoNUOsqOnV9u0veYUfEj00mj3VIed0'
    }

    return render(request, template, context)