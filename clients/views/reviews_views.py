from django.shortcuts import render
from django.http import JsonResponse
from ..models import Review
from  auditors.models import AuditorProfile
import json


def client_review(request):
    if request.method == 'POST':
        
        try:
            data = json.loads(request.body)
            client = request.user.clientprofile
            auditor = AuditorProfile.objects.get(id = data['auditor_id'])
            vote = data['vote']
            review, created = Review.objects.get_or_create(
                client_profile= client,
                auditor_profile= auditor,
                defaults={'value': vote}
            )
            if not created:
                review.value = vote
                review.save()
            review_up_count = Review.objects.filter(auditor_profile = auditor, value = 'up').count()
            review_down_count = Review.objects.filter(auditor_profile = auditor, value = 'down').count()
            
            return JsonResponse({
                'message': 'Todo joya',
                'review_up_count': review_up_count,
                'review_down_count': review_down_count,
                })
        except Exception as e:
            print("Error guardando review,", e)
            return JsonResponse({'error': str(e)}, status=400)
        
    
    
        