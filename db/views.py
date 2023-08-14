from django.db.models import Count
from .models import *

def create_genre_recommendations(user):
    listened_genres = ListeningHistory.objects.filter(user=user).values('music__genre_name').annotate(total_points=Count('id'))
    
    max_points = 8  
    recommendations = []
    
    for genre_data in listened_genres:
        genre = Genre.objects.get(pk=genre_data['music__genre_name'])
        total_points = min(genre_data['total_points'], max_points)
        
        recommendation, created = Recommendations.objects.get_or_create(user=user, genre=genre, defaults={'total_points': total_points})
        
        if not created:
            recommendation.total_points = total_points
            recommendation.save()
        
        recommendations.append(recommendation)
    
    return recommendations
