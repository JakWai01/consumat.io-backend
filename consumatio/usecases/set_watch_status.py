def set_watch_status(database: object, external_id: str, code: int, media: str,
                     watchStatus: str) -> dict:
    """
    Set watch_status for a particular Movie or TV
    :param database: <object> Database object to access database
    :param external_id: <int> External ID provided by OAuth
    :param code: <int> Code of the media to set watchStatus for
    :param media: <str> Type of media
    :param watchStatus: <str> WatchStatus, one of ["Movie", "TV", "Season", "Episode"]
    :return: <dict: Successful response
    """
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    if not database.media_data_exists(user_id, media, code):
        database.media_Data(user_id, media, code, tv_code=None)

    database.watch_status(user_id, media, code, watchStatus)
    return {"status": True}