from collections import namedtuple

from graphene import ObjectType, String, Field, Schema

PersonValueObject = namedtuple("Person", ["first_name", "last_name"])

class Person(ObjectType):
    first_name = String()
    last_name = String()

class Query(ObjectType):
    me = Field(Person, id=String())
    my_best_friend = Field(Person)

    def resolve_me(parent, info, id):
        # always pass an object for `me` field
        
        # assume this is the movie(id: 2) { title }
        # then we call the use_case here (e.g. get_movie_details(tmdb, id))
        # we return a new movie instead with the provided information from the api above with id = 1
        print(id)
        return PersonValueObject(first_name="Luke", last_name="Skywalker")

    def resolve_my_best_friend(parent, info):
        # always pass a dictionary for `my_best_fiend_field`
        return {"first_name": "R2", "last_name": "D2"}

schema = Schema(query=Query)
result = schema.execute('''
    {
        me(id: "2") { 
            firstName
            lastName 
        }
        myBestFriend { firstName lastName }
    }
''')
# With default resolvers we can resolve attributes from an object..
assert result.data["me"] == {"firstName": "Luke", "lastName": "Skywalker"}

# With default resolvers, we can also resolve keys from a dictionary..
assert result.data["myBestFriend"] == {"firstName": "R2", "lastName": "D2"}

print(result.data["me"])