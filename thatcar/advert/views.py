from django.views.decorators.http import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@require_GET
def get_advert_by_id(request, advert_id):
    return JsonResponse(
        {
            'id': advert_id,
            'user': 'Thatcar User',
            'car': 'Volkswagen Golf VII',
            'price': 1_000_000,
            'milage': 120_000,
            'color': 'Dark Blue',
            'vin': 'WVWZZZAUZEW000001',
            'power': 122
        }
    )


@require_GET
def get_adverts_by_color_id(request, color_id):
    return JsonResponse(
        {
            'color_id': color_id,
            'color': 'Dark Blue',
            'adverts': [
                {
                    'id': 1,
                    'user': 'Thatcar User',
                    'car': 'Volkswagen Golf VII',
                    'price': 1_000_000,
                    'milage': 120_000,
                    'color': 'Dark Blue',
                    'vin': 'WVWZZZAUZEW000001',
                    'power': 122
                },
                {
                    'id': 2,
                    'user': 'Thatcar User',
                    'car': 'Audi A3',
                    'price': 1_200_000,
                    'milage': 75_000,
                    'color': 'Pearl White',
                    'vin': 'WVWOOOAUZLK002001',
                    'power': 125
                }
            ]
        }
    )


@require_GET
def get_all_adverts(request):
    return JsonResponse(
        {
            'adverts': [
                {
                    'id': 1,
                    'user': 'Thatcar User',
                    'car': 'Volkswagen Golf VII',
                    'price': 1_000_000,
                    'milage': 120_000,
                    'color': 'Dark Blue',
                    'vin': 'WVWZZZAUZEW000001',
                    'power': 122
                },
                {
                    'id': 2,
                    'user': 'Thatcar User',
                    'car': 'Audi A3',
                    'price': 1_200_000,
                    'milage': 75_000,
                    'color': 'Pearl White',
                    'vin': 'WVWZZZAUTGW420011',
                    'power': 125
                }
            ]
        }
    )


@csrf_exempt
@require_POST
def post_advert(request):
    return JsonResponse(
        {
            'code': 200,
            'message': f'Advert was successfully published'
        }
    )
