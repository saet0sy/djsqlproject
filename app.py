from django.db.models import Count
from db.models import Users, Genre, Album, Music, ListeningHistory, Recommendations


def create_genre_recommendations(user):
    listened_genres = (
        ListeningHistory.objects
        .filter(user=user)
        .values('music__genre_name')
        .annotate(total_points=Count('id'))
        .order_by('-total_points')  # Сортируем по убыванию баллов
    )

    max_points = 8
    recommendations = []

    # Увеличиваем баллы для жанра с самым большим количеством баллов
    if listened_genres:
        most_listened_genre_data = listened_genres[0]
        most_listened_genre = Genre.objects.get(pk=most_listened_genre_data['music__genre_name'])
        total_points = min(most_listened_genre_data['total_points'] * 2, max_points)

        recommendation, created = Recommendations.objects.get_or_create(
            user=user,
            genre=most_listened_genre,
            defaults={'total_points': total_points}
        )

        if not created:
            recommendation.total_points = total_points
            recommendation.save()

        recommendations.append(recommendation)

    return recommendations


def main():
    # Создаем или получаем пользователя
    user, created = Users.objects.get_or_create(username='john_doe')

    # Создаем или получаем жанры
    genre_pop, created = Genre.objects.get_or_create(genre_name='Поп')
    genre_rock, created = Genre.objects.get_or_create(genre_name='Рок')
    genre_jazz, created = Genre.objects.get_or_create(genre_name='Джаз')

    # Создаем или получаем альбомы
    album_thriller, created = Album.objects.get_or_create(album_name='Thriller', album_year='1982-01-01')
    album_metallica, created = Album.objects.get_or_create(album_name='Metallica', album_year='1991-08-12')
    album_kind_of_blue, created = Album.objects.get_or_create(album_name='Kind of Blue', album_year='1959-08-17')

    # Создаем или получаем музыку
    music_billie_jean, created = Music.objects.get_or_create(
        music_name='Billie Jean',
        album_name=album_thriller,
        genre_name=genre_pop,
        music_year='1982-01-01'
    )
    music_enter_sandman, created = Music.objects.get_or_create(
        music_name='Enter Sandman',
        album_name=album_metallica,
        genre_name=genre_rock,
        music_year='1991-08-12'
    )
    music_so_what, created = Music.objects.get_or_create(
        music_name='So What',
        album_name=album_kind_of_blue,
        genre_name=genre_jazz,
        music_year='1959-08-17'
    )

    # Создаем или получаем историю прослушиваний
    listening_history_1, created = ListeningHistory.objects.get_or_create(
        user=user,
        music=music_billie_jean,
        genre_points=1
    )
    listening_history_2, created = ListeningHistory.objects.get_or_create(
        user=user,
        music=music_enter_sandman,
        genre_points=1
    )
    listening_history_3, created = ListeningHistory.objects.get_or_create(
        user=user,
        music=music_so_what,
        genre_points=1
    )

    # Создаем рекомендации для пользователя на основе прослушанных жанров
    recommendations = create_genre_recommendations(user)

    # Выводим пользователю рекомендации
    print("Рекомендации для пользователя", user)
    for recommendation in recommendations:
        print("Жанр:", recommendation.genre.genre_name)
        print("Баллы:", recommendation.total_points)
        print("---")


if __name__ == "__main__":
    main()