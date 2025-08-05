from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    description = fields.Str(required=True, validate=validate.Length(min=1))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class TaskCreateSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1, max=255))
    description = fields.Str(required=True, validate=validate.Length(min=1))

class TaskUpdateSchema(Schema):
    title = fields.Str(validate=validate.Length(min=1, max=255), allow_none=False)
    description = fields.Str(validate=validate.Length(min=1), allow_none=False) 