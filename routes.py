from resources import Base, HealthCheck

def setup_routes(api):
    api.add_resource(HealthCheck, '/')
    api.add_resource(Base, '/v1/health')

