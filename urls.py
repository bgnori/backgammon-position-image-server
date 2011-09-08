from werkzeug.routing import Map, Rule

url_map = Map([
  Rule("/", endpoint="index"),
  Rule("/about", endpoint="about"),
  Rule("/image", endpoint="image"), #old dog
  Rule("/gnubg", endpoint="gnubg"),
  Rule("/xgid", endpoint="xgid"),
  Rule("/errors/", endpoint="list_errors"),
  Rule("/errors/400", endpoint="bad_request"),
  Rule("/errors/401", endpoint="unauthorized"),
  Rule("/errors/404", endpoint="not_found"),
  Rule("/errors/405", endpoint="method_not_allowed"),
  Rule("/errors/406", endpoint="not_acceptable"),
  Rule("/errors/408", endpoint="request_timeout"),
  Rule("/errors/412", endpoint="precondition_failed"),
  Rule("/errors/413", endpoint="request_entity_too_large"),
  Rule("/errors/414", endpoint="request_uri_too_long"),
  Rule("/errors/415", endpoint="unsupported_media_type"),
  Rule("/errors/417", endpoint="expectation_failed"),
  Rule("/errors/418", endpoint="Im_python"),
  Rule("/errors/500", endpoint="internal_server_error"),
  Rule("/errors/501", endpoint="not_implemented"),
])

