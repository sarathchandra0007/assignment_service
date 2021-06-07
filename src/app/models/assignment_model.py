"""
Assignment model
"""
from . import db
from sqlalchemy.sql import func

# Helper table for many to many relationship between tags and assignments
assignment_tags = db.Table('tags',
                           db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                           db.Column('assignment_id', db.Integer, db.ForeignKey('assignment.id'), primary_key=True)
                           )


class Assignment(db.Model):
    """Assignment Model"""
    __tablename__ = 'assignment'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    type = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    tags = db.relationship('Tag', secondary=assignment_tags,
                           backref=db.backref('assignments', lazy='dynamic'))

    def __str__(self):
        return self.name

    def __init__(self, name, title, type, duration, description=''):
        self.name = name
        self.title = title
        self.description = description
        self.type = type
        self.duration = duration

    def _get_tags(self):
        """Get all tag names for an assignment"""
        return [x.name for x in self.tags]

    def _set_tags(self, value):
        """Set all tags while creation"""
        for tag in value:
            self.tags.append(self._find_or_create_tag(tag))

    @staticmethod
    def _find_or_create_tag(tag):
        """Create Tags in Tag model"""
        q_set = Tag.query.filter_by(name=tag)
        tag_obj = q_set.first()
        if not tag_obj:
            tag_obj = Tag(tag)
        return tag_obj

    def save(self):
        """Db call to save data"""
        db.session.add(self)
        db.session.commit()
        return self


class Tag(db.Model):
    """Tag model"""
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
