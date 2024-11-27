from flask import Blueprint, current_app
from configs.conecction import collections
from .controller import (
    create_event,
    create_many_events,
    get_all_events,
    get_event_by_id,
    get_events_by_reproductive_id,
    update_event,
    delete_event,
    get_event_by_bovino_id,
    get_reproductive_by_finca_id
)

# Crear Blueprint
reproductive_event_blueprint = Blueprint("reproductive_event", __name__)

@reproductive_event_blueprint.route("/", methods=["POST"])
def create():
    return create_event(collections)

@reproductive_event_blueprint.route("/batch", methods=["POST"])
def create_many():
    return create_many_events(collections)

@reproductive_event_blueprint.route("/", methods=["GET"])
def get_all():
    return get_all_events(collections)

@reproductive_event_blueprint.route("/<event_id>", methods=["GET"])
def get_by_id(event_id):
    return get_event_by_id(collections, event_id)

@reproductive_event_blueprint.route("/cattle/<reproductiveId>", methods=["GET"])
def get_by_reproductive_id(reproductiveId):
    return get_events_by_reproductive_id(collections, reproductiveId)

@reproductive_event_blueprint.route("/<event_id>", methods=["PUT"])
def update(event_id):
    return update_event(collections, event_id)

@reproductive_event_blueprint.route("/<event_id>", methods=["DELETE"])
def delete(event_id):
    return delete_event(collections, event_id)

@reproductive_event_blueprint.route("/bovino/<bovino_id>", methods=["GET"])
def get_event_by_bovino_id_route(bovino_id):
    return get_event_by_bovino_id(collections, bovino_id)
  
@reproductive_event_blueprint.route("/finca/<finca_id>", methods=["GET"])
def get_event_by_finca_id_route(finca_id):
    return get_reproductive_by_finca_id(collections, finca_id)
