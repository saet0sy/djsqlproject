# from django.shortcuts import render
# from db.models import Users, Genre, Album, Music, ListeningHistory, Recommendations
# from db.views import create_genre_recommendations
# from django.db.models import Count

# # Создание пользователя
# user = Users.objects.create(username='username1')

# # Получение всех пользователей
# all_users = Users.objects.all()

# # Создание жанра
# genre = Genre.objects.create(genre_name='Rock')

# # Создание альбома
# album = Album.objects.create(album_name='Album 1', album_year='2023-01-01')

# # Получение жанра
# genre = Genre.objects.get(genre_name='Rock')

# # Создание музыки
# music = Music.objects.create(music_name='Song 1', album_name=album, genre_name=genre, music_year='2023-01-01')

# # Запись истории прослушивания
# ListeningHistory.objects.create(user=user, music=music, genre_points=1)

# # Создание рекомендаций
# recommendations = create_genre_recommendations(user)

