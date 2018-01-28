import graphene

import cookbook.ingredients.schema as cookbook_schema


class Query(cookbook_schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
