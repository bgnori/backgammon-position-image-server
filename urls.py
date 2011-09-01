from werkzeug.routing import Map, Rule

url_map = Map([
  Rule("/", endpoint="index"),
  Rule("/foofoo", endpoint="foofoo"),
  Rule("/errors/404", endpoint="not_found"),
  Rule("/errors/500", endpoint="internal_server_error"),
])
