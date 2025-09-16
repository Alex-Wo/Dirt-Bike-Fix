from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Factory, Bike


def bike_list(request):
    factories = Factory.objects.all()
    bikes = Bike.objects.all()
    context = {
        'factories': factories,
        'bikes': bikes,
    }
    return render(request, 'manuals/bike_list.html', context)


def bike_detail(request, factory_id=None):
    factory = None
    bikes = Bike.objects.all()

    if factory_id:
        try:
            # Получаем конкретный 'factory'
            factory = get_object_or_404(Factory, id=factory_id)

            # Получаем все 'bike' этого 'factory'
            bikes = Bike.objects.filter(factory=factory)

        except Factory.DoesNotExist:
            raise Http404("Фабрика не найдена")

    context = {
        'factory': factory,  # Текущий 'factory' (если есть)
        # 'factories': Factory.objects.all(),  # Все 'factory' фабрики для навигации
        'bikes': bikes,  # Список велосипедов
    }

    return render(request, 'manuals/bike_detail.html', context)
