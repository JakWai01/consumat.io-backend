def set_watch_status(database, external_id, code, media, watchStatus):
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    if not database.media_data_exists(user_id, media, code):
        database.media_Data(user_id, media, code)

    database.watch_status(user_id, media, code, watchStatus)
    return {"status": True}