from consumatio.gateways.movie_providers_to_dict import * 

def test_movie_providers_to_dict():
    json = {
      "link": "https://www.themoviedb.org/movie/550-fight-club/watch?locale=AR",
      "flatrate": [
        {
          "display_priority": 1,
          "logo_path": "/68MNrwlkpF7WnmNPXLah69CR5cb.jpg",
          "provider_id": 119,
          "provider_name": "Amazon Prime Video"
        },
        {
          "display_priority": 7,
          "logo_path": "/rgbalNWbAuhWklHH5JAnF53Wjey.jpg",
          "provider_id": 339,
          "provider_name": "Movistar Play"
        }
      ],
      "rent": [
        {
          "display_priority": 2,
          "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
          "provider_id": 2,
          "provider_name": "Apple iTunes"
        },
        {
          "display_priority": 3,
          "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
          "provider_id": 3,
          "provider_name": "Google Play Movies"
        },
        {
          "display_priority": 8,
          "logo_path": "/mzu37NQphDvqN2BHKM0Rwq9Es3r.jpg",
          "provider_id": 167,
          "provider_name": "Claro video"
        }
      ],
      "buy": [
        {
          "display_priority": 2,
          "logo_path": "/q6tl6Ib6X5FT80RMlcDbexIo4St.jpg",
          "provider_id": 2,
          "provider_name": "Apple iTunes"
        },
        {
          "display_priority": 3,
          "logo_path": "/p3Z12gKq2qvJaUOMeKNU2mzKVI9.jpg",
          "provider_id": 3,
          "provider_name": "Google Play Movies"
        }
      ]
    }

    print(movie_providers_to_dict(json))
    dict = {
        'providers': [
            'Amazon Prime Video', 
            'Movistar Play'
        ]
    }

    assert movie_providers_to_dict(json) == dict