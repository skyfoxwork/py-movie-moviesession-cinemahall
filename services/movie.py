import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Movie


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    if not genres_ids and not actors_ids:
        print("not genres_ids and actors_ids")
        return Movie.objects.all()

    if genres_ids and actors_ids:
        print("genres_ids and actors_ids")
        # return Movie.objects.filter(genres__in=genres_ids).filter()
        return Movie.objects.filter(genres__id__in=genres_ids).filter(actors__id__in=actors_ids)

    if genres_ids:
        print("genres_ids")
        return Movie.objects.filter(genres__id__in=genres_ids)

    if actors_ids:
        print("actors_ids")
        return Movie.objects.filter(actors__id__in=actors_ids)


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None
) -> Movie:
    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description
    )

    if actors_ids:
        new_movie.actors.set(actors_ids)

    if genres_ids:
        new_movie.genres.set(genres_ids)

    return new_movie


if __name__ == '__main__':
    # print(get_movies())
    # print(get_movies(genres_ids=[1, 2], actors_ids=[1, 2]))
    # print(get_movies(genres_ids=[1, 2]))
    # print(get_movies(actors_ids=[1, 2]))

    # print(get_movie_by_id(1))

    # movie = create_movie(
    #     movie_title="Blade Runner",
    #     movie_description="Movie about future",
    #     genres_ids=[5, 6],
    #     actors_ids=[1, 2]
    # )
    # print(movie)

    pass
