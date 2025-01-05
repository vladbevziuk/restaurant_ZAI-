from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm

def index(request):
    return render(request, 'main/index.html')

def order_table(request):
    return render(request, 'main/order_table.html')

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            return redirect('order_success', success=True)  # Перенаправление с успешным результатом
        else:
            return redirect('order_success', success=False)  # Перенаправление с неуспешным результатом
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'form': form})

def order_success(request, success):
    message = "Ваш заказ успешно оформлен!" if success else "Ошибка при оформлении заказа."
    return render(request, 'main/order_success.html', {'message': message})
