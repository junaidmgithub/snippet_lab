class Connections:

    connection = None

    def __init__(self, **configs):
        self.connections = {}
        self.configs = configs

    def get_connection(self, alias='default'):
        try:
            return self.connections[alias]
        except KeyError:
            pass
        return self.create_connection(alias, **self.configs[alias])

    def create_connection(self, alias="default", **kwargs):
        self.connections[alias] = dict(**kwargs) # // change stub here
        return self.connections[alias]

    def add_connection(self, alias, conn):
        self.connections[alias] = conn

    def configure(self, **kwargs):
        self.configs.update(kwargs)


connections = Connections(default={'host':'127.0.0.1', 'port': 5600},
                          dev={'host':'', 'port': 123},
                          qa={})
configure = connections.configure
add_connection = connections.add_connection
create_connection = connections.create_connection
get_connection = connections.get_connection


# Usage
print(get_connection())
print(get_connection('dev'))
print(get_connection('dev'))
print(get_connection('qa'))
