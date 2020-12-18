from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView

from .models import Pizza, Order


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizza_list'] = Pizza.objects.all()
        context['orders'] = Order.objects.filter(user=self.request.user)
        return context


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order.html'


class OrderPizza(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            pizza = Pizza.objects.get(id=request.POST.get('pizza_id'))
        except Pizza.DoesNotExist:
            return JsonResponse({'error': 'Something went wrong'}, status=422)
        else:
            order = Order(user=user, pizza=pizza, amount=pizza.price)
            order.save()
            return JsonResponse({'message': 'Success'})

