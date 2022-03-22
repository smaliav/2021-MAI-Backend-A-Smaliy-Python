from django.http.response import JsonResponse
from django.views.decorators.http import *
from random import randint


MAX_ID = 100_000


@require_GET
def get_profile(request, profile_id):
    return JsonResponse(
        {
            'id': profile_id,
            'firstName': 'User',
            'lastName': 'Thatcar',
            'about': 'Just a Thatcar User and a good man.'
        }
    )


@require_GET
def get_car(request, car_id):
    return JsonResponse(
        {
            'id': car_id,
            'brand': 'Brand',
            'model': 'Model',
            'year': 2022,
        }
    )


@require_GET
def get_cars(request):
    return JsonResponse(
        {
            'cars': [
                {
                    'id': randint(0, MAX_ID),
                    'brand': 'Volkswagen',
                    'model': 'Golf VII',
                    'year': 2014,
                },
                {
                    'id': randint(0, MAX_ID),
                    'brand': 'Audi',
                    'model': 'Q3',
                    'year': 2015,
                },
                {
                    'id': randint(0, MAX_ID),
                    'brand': 'BMW',
                    'model': '340i',
                    'year': 2017,
                }
            ]
        }
    )


@require_GET
def get_category(request, category):
    return JsonResponse(
        {
            'category': category,
            'description': 'Category description',
            'positions': [
                {
                    'id': randint(0, MAX_ID),
                    'brand': 'Volkswagen',
                    'model': 'Golf VII',
                    'year': 2014,
                },
                {
                    'id': randint(0, MAX_ID),
                    'brand': 'Audi',
                    'model': 'Q3',
                    'year': 2015,
                },
                {
                    'id': randint(0, MAX_ID),
                    'brand': 'BMW',
                    'model': '340i',
                    'year': 2017,
                }
            ]
        }
    )
