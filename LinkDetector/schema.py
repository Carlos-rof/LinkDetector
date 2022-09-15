import graphene
import detector.schema


class Query(detector.schema.Query, graphene.ObjectType):
    pass


class Mutation(detector.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


# {"query":"query {urls {id fullUrl urlHash clicks createdAt}}"}
# {"query":"mutation {createUrl(fullUrl:\"%s\") {url {id fullUrl urlHash clicks createdAt}}}"}

