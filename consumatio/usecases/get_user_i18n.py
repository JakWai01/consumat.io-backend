from consumatio.external.db.models import *


def get_user_i18n(external_id: str, db: object) -> dict:
    """
    Get i18n  for current user
    :param external_id: <str> External ID provided by OAuth
    :return: <dict> dict with country and language fields
    """

    # user = User.query.filter_by(external_id_content=external_id).first()
    user = db.session.query(User).filter_by(
        external_id_content=external_id).first()
    user_country = user.country
    user_language = user.language

    return {
        "country": user_country,
        "language": user_language,
    }
