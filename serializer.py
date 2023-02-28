from models import TodoList
from app import ma

# create schema
class TodoSchema(ma.Schema):
    class Meta:
        model = TodoList
        fields = ("title", "description", "date_created", "completed")


todoSchema = TodoSchema(many=False)
todoSchemas = TodoSchema(many=True)