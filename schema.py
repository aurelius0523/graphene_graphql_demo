"""docstring"""
import graphene

import cookbook.ingredients.schema as cookbook_schema

class Query(cookbook_schema.Query, graphene.ObjectType):
    """Graphene standard definition. No implementation needed"""
    pass


SCHEMA = graphene.Schema(query=Query)
