def set_language(database: object, external_id: str, language: str) -> dict:
    """
    Set language for the current user
    :param database: <object> Database object to access database
    :param external_id: <int> External ID provided by OAuth
    :param language: <str> RFC 5646 BCP language tag (e.g. 'de-DE' or 'en-US')
    :return: <dict> Successful response
    """
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    database.user_language(user_id, language)

    return {"status": True}