# -*- coding: utf-8 -*-
import logging

from pyramid.events import NewRequest
from pyramid.settings import asbool

from pyramid_rest.resource import ResourceUtility

log = logging.getLogger(__name__)


class RequestMethodEventPredicate(object):

    def __init__(self, methods, config):
        self.methods = methods

    def __call__(self, event):
        return event.request.method in self.methods


def override_request_method(event):
    methods = ['PUT', 'DELETE']
    override = (
        event.request.headers.get('X-HTTP-Method-Override') or
        event.request.GET.get('_method', '').upper()
        )

    if override in methods:
        event.request.method = override


def includeme(config):
    log.info('Includes pyramid_rest')
    config.registry.registerUtility(ResourceUtility(config))

    if asbool(config.registry.settings.get(
        'pyramid_rest.tunneling',
        'true',
        )):
        config.add_subscriber_predicate(
            'request_methods',
            RequestMethodEventPredicate
            )

        config.add_subscriber(
            override_request_method,
            NewRequest,
            request_methods=['POST'],
            )
