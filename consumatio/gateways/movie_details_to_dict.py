def movie_details_to_dict(data):
       dict = {
           "code": data["id"],
           "title": data["original_title"],
           "genres": data["genres"],
           "overview": data["overview"],
           "popularity": data["popularity"],
           "release_date": data["release_date"],
           "runtime": data["runtime"],
           "status": data["status"]
       }

       return dict
