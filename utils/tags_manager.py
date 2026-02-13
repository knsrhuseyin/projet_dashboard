import json

from db.models import Tag

def add_tag(tags_name: str, db):
    tag = Tag.query.filter_by(name=tags_name).first()
    if not tag:
        tag = Tag(name=tags_name)
        db.session.add(tag)
        db.session.commit()
    return tag

def get_tag(name):
    return Tag.query.filter_by(name=name).first()

def get_page_tags(request) -> list | bool:
    if request.form.get("tags_json", "[]"):
        return json.loads(request.form.get("tags_json", "[]"))
    else:
        return False