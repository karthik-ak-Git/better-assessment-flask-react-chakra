from flask import Blueprint, request, jsonify
from app.schemas.comment import CommentSchema
from app.services.comment_service import CommentService

comment_bp = Blueprint("comments", __name__)
schema = CommentSchema()


@comment_bp.route("/api/comments", methods=["POST"])
def create_comment():
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    comment = CommentService.create_comment(data)
    return schema.dump(comment), 201


@comment_bp.route("/api/comments/<int:task_id>", methods=["GET"])
def get_comments(task_id):
    page = request.args.get("page", default=1, type=int)
    limit = request.args.get("limit", default=10, type=int)
    comments = CommentService.get_comments(task_id, page, limit)
    return schema.dump(comments, many=True), 200


@comment_bp.route("/api/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    data = request.get_json()
    comment = CommentService.update_comment(comment_id, data)
    if not comment:
        return jsonify({"error": "Not found"}), 404
    return schema.dump(comment), 200


@comment_bp.route("/api/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    comment = CommentService.delete_comment(comment_id)
    if not comment:
        return jsonify({"error": "Not found"}), 404
    return jsonify({"msg": "Deleted"}), 200
