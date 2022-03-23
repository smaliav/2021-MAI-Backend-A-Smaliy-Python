from django.views.decorators.http import require_GET
from django.http import JsonResponse


@require_GET
def get_car_by_id(request, car_id):
    return JsonResponse(
        {
            'id': car_id,
            'brand': 'Volkswagen',
            'model': 'Golf VII',
            'year': 2014,
            'category': "City Hatch"
        }
    )


@require_GET
def get_cars_by_brand_name(request, brand_name):
    return JsonResponse(
        {
            'brand': brand_name,
            'cars': [
                {
                    'id': 1,
                    'brand': brand_name,
                    'model': 'Golf VII',
                    'year': 2014,
                    'category': "City Hatch"
                },
                {
                    'id': 2,
                    'brand': brand_name,
                    'model': 'Passat',
                    'year': 2011,
                    'category': "City sedan"
                },
                {
                    'id': 3,
                    'brand': brand_name,
                    'model': 'Tiguan',
                    'year': 2019,
                    'category': "City Crossover"
                }
            ]
        }
    )


@require_GET
def get_cars_by_category_id(request, category_id):
    return JsonResponse(
        {
            'category_id': category_id,
            'category': 'City Hatch',
            'cars': [
                {
                    'id': 1,
                    'brand': 'Volkswagen',
                    'model': 'Golf VII',
                    'year': 2014,
                    'category': "City Hatch"
                },
                {
                    'id': 4,
                    'brand': 'Audi',
                    'model': 'A3',
                    'year': 2020,
                    'category': "City Hatch"
                },
                {
                    'id': 5,
                    'brand': 'Mini',
                    'model': 'Cooper',
                    'year': 2010,
                    'category': "City Hatch"
                }
            ]
        }
    )
