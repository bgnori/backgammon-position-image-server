from werkzeug.routing import Map, Rule

url_map = Map([
  Rule("/", endpoint="index"),
  Rule("/about", endpoint="about"),
  Rule("/image", endpoint="image"), #old dog
  Rule("/gnubg", endpoint="gnubg"),
  Rule("/xgid", endpoint="xgid"),
  Rule("/errors/404", endpoint="not_found"),
  Rule("/errors/500", endpoint="internal_server_error"),
])

