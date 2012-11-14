* Force human-friendly names for route pattern variables and view callable
  parameters, e.g. /applications/{application_id}/users/{id} and
  show(context, request, application_id, id)
* Remove ability to configure resource separator in resource names: it's always
  '.'
* Singular resources via *add_singular_resource* directive or *singular=True*
  keyword argument on *Resource* or *resource_config*
* Moved example from tests directory to root directory: used in test and useful
  for documentation.

0.0.1
-----
* Collection resource only
* Imperative mode via *add_resource* directive
* Declarative mode via *Resource* class
* Declarative mode view *resource_config* decorator