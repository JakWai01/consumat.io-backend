def set_rating(database: object, external_id: str, media: str, code: int,
               rating: int) -> dict:
    """
    Set rating for a particular Movie/ TV Show
    :param tmdb: <object> TMDB object to make API requests
    :param database: <object> Database object to access the database
    :param external_id: <str> External ID provided by OAuth
    :param media: <str> Type of media to set rating for
    :param code: <int> Code of the media
    :param rating: <int> rating
    :return: <dict> Successful response
    """
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    if not database.media_data_exists(user_id, media, code):
        database.media_Data(user_id, media, code, tv_code=None)

    database.rating(user_id, media, code, rating)
    return {"status": True}