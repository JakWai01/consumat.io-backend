from consumatio.external.models import *
from sqlalchemy import text


class WatchCount:
    def get_watch_count(self, database, user, type):
        count = 0
        results = MediaData.query.from_statement(
            text(
                "SELECT * FROM media_data, user_data WHERE user_data.user_id_content = media_data.user_id_content_media_data AND media_data.media_type_content = :type AND user_data.external_id_content = :user;"
            )).params(user=user, type=type).all()

        for i in range(len(results)):
            count += 1

        return count
