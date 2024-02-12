post_create = {
  "type": "object",
  "properties": {
    "test1": {
      "type": "string"
    },
    "test2": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    }
  },
  "required": [
    "test1",
    "test2",
    "id"
  ], "additionalProperties": False
}
put_response = {
  "type": "object",
  "properties": {
    "test0": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    }
  },
  "required": [
    "test0",
    "id"
  ]
}
patch_change = {
  "type": "object",
  "properties": {
    "title": {
      "type": "string"
    },
    "body": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "userId": {
      "type": "integer"
    }
  },
  "required": [
    "title",
    "body",
    "id",
    "userId"
  ], "additionalProperties": False
}
delete_response = {}
