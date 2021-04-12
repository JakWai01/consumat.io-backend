import graphene
from graphene import Decimal

class Patron(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()

class Query(graphene.ObjectType):
    patron = graphene.Field(Patron, code=Decimal())
    
    def resolve_patron(root, info, code):
        print(code)
        return Patron(id=1, name="Syrus", age=27)

schema = graphene.Schema(query=Query)
query = """
    query something {
        patron(code: "3") {
            id
            name
        }
    }
"""

def test_query():
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {"patron": {"id": "1", "name": "Syrus", "age": 27}}

if __name__ == "__main__":
    result = schema.execute(query)
    print(result.data["patron"])