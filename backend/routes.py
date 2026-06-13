from flask import Blueprint, request, jsonify  # type: ignore

kudos_routes = Blueprint("kudos", __name__)

# In-memory store for demo purposes
_kudos_store = []


@kudos_routes.route("/", methods=["GET"])
def list_kudos():
    return jsonify(_kudos_store), 200


@kudos_routes.route("/", methods=["POST"])
def create_kudo():
    data = request.get_json() or {}
    sender = data.get("sender_id")
    recipient = data.get("recipient_id")
    message = data.get("message")
    if not sender or not recipient or not message:
        return jsonify({"error": "sender_id, recipient_id, and message are required"}), 400
    k = {
        "id": len(_kudos_store) + 1,
        "sender_id": sender,
        "recipient_id": recipient,
        "message": message,
        "is_visible": True,
    }
    _kudos_store.append(k)
    return jsonify(k), 201