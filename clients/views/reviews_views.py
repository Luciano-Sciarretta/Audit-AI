from django.shortcuts import render
from django.http import JsonResponse
from ..models import Review
from  auditors.models import AuditorProfile
import json


def client_review(request):
    if request.method == 'POST':
        
        try:
            # print("PRINT_1:",type(request.body))
            data = json.loads(request.body)
            # print("PRINT_2:", data)
            client = request.user.clientprofile
            # print("PRINT_3:",  client)
            auditor = AuditorProfile.objects.get(id = data['auditor_id'])
            vote = data['vote']
            # print("PRINT_4:", auditor, vote)
            review = Review(
                client_profile= client,
                auditor_profile= auditor,
                value= vote  
            )
            # print("Review:", review)
            review.save()
            review_count = Review.objects.filter(auditor_profile = auditor, value = 'up').count()
            print("Count:", review_count)
            return JsonResponse({
                'message': 'Todo joya',
                'review_count': review_count
                })
        except Exception as e:
            print("Error guardando review,", e)
            return JsonResponse({'error': str(e)}, status=400)
        
    
    
        