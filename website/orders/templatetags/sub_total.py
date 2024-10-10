from django import template

register = template.Library()
@register.simple_tag(name = 'sub_total')
def sub_total(cart):
    total=0
    for item in cart.added_items.all():
        total+=item.quantity*item.product.price
    return total