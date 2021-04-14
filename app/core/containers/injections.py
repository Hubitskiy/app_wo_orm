from .container import Container

from users.injections import dependencies as user_dependencies


_dependencies = set()

container = Container()

_dependencies.update(user_dependencies)

container.register_set_dependencies(_dependencies)

resolve = container.resolve
