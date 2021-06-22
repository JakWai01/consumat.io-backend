from consumatio.external.db.models import User


def get_user_i18n(external_id: str, db: object) -> dict:
    """
    Get i18n  for current user
    :param external_id: <str> External ID provided by OAuth
    :param db: <object> Database object
    :return: <dict> Dict with country and language fields
    """

    user = db.session.query(User).filter_by(
        external_id_content=external_id).first()

    if user is None:
        user = User(external_id)
        db.session.add(user)
        db.session.commit()

    user_country = user.country
    user_language = user.language

    return {
        "country": user_country,
        "language": user_language,
    }
