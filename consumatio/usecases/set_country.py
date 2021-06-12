def set_country(database: object, external_id: str, country: str) -> dict:
    """
    Set country for the current user
    :param database: <object> Database object to access database
    :param external_id: <int> External ID provided by OAuth
    :param country: <str> ISO 3166-1 alpha-2 country code (e.g. 'DE' or 'US')
    :return: <dict> Successful response
    """
    user_id = 0

    if not database.user_exists(external_id):
        database.user(external_id)
    user_id = database.get_user_id(external_id)

    database.user_country(user_id, country)

    return {"status": True}