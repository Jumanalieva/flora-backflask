from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()
db = SQLAlchemy()

class Blog(db.Model):
    __tablename__ = 'blog'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing integer ID
    title = db.Column(db.String(150), nullable=False)
    short_description = db.Column(db.String(300), nullable=False)
    questions = db.Column(db.JSON, nullable=True)  # List of questions
    answers = db.Column(db.JSON, nullable=True)    # List of answers
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    images = db.Column(db.JSON)                    # List of image URLs
    videos = db.Column(db.JSON)                    # List of video URLs

    def __init__(self, title, short_description, questions, answers, images=None, videos=None):
        self.title = title
        self.short_description = short_description
        self.questions = questions or []
        self.answers = answers or []
        self.images = images or []
        self.videos = videos or []

    def __repr__(self):
        return f'<Blog {self.title}: {self.short_description}>'

class Culinary(db.Model):
    __tablename__ = 'culinary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(300), nullable=False)
    questions = db.Column(db.JSON, nullable=True)  # List of questions
    answers = db.Column(db.JSON, nullable=True)    # List of answers
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    images = db.Column(db.JSON)                    # List of image URLs
    videos = db.Column(db.JSON)                    # List of video URLs

    def __init__(self, title, short_description, questions, answers, images=None, videos=None):
        self.title = title
        self.short_description = short_description
        self.questions = questions or []
        self.answers = answers or []
        self.images = images or []
        self.videos = videos or []

    def __repr__(self):
        return f'<Culinary {self.title}>'

class Culture(db.Model):
    __tablename__ = 'culture'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing integer ID
    title = db.Column(db.String(150), nullable=False)
    short_description = db.Column(db.String(300), nullable=False)
    questions = db.Column(db.JSON, nullable=True)  # List of questions
    answers = db.Column(db.JSON, nullable=True)    # List of answers
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    images = db.Column(db.JSON)                    # List of image URLs
    videos = db.Column(db.JSON)                    # List of video URLs

    def __init__(self, title, short_description, questions, answers, images=None, videos=None):
        self.title = title
        self.short_description = short_description
        self.questions = questions or []
        self.answers = answers or []
        self.images = images or []
        self.videos = videos or []

    def __repr__(self):
        return f'<Culture {self.title}>'

class Media(db.Model):
    __tablename__ = 'media'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Auto-incrementing integer ID
    media_type = db.Column(db.String(10), nullable=False)  # e.g., "image" or "video"
    media_url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    
    # Generic fields for associations
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=True)
    culinary_id = db.Column(db.Integer, db.ForeignKey('culinary.id'), nullable=True)
    culture_id = db.Column(db.Integer, db.ForeignKey('culture.id'), nullable=True)

    def __init__(self, media_type, media_url, description=None, blog_id=None, culinary_id=None, culture_id=None):
        self.media_type = media_type
        self.media_url = media_url
        self.description = description
        self.blog_id = blog_id
        self.culinary_id = culinary_id
        self.culture_id = culture_id

    def __repr__(self):
        return f'<Media {self.media_type} - {self.media_url}>'

# Schemas
class BlogSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'short_description', 'questions', 'answers', 'created_at', 'images', 'videos']

    questions = fields.List(fields.String())
    answers = fields.List(fields.String())

blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)

# Culinary Schema
class CulinarySchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'short_description', 'questions', 'answers', 'created_at', 'images', 'videos']

    questions = fields.List(fields.String())
    answers = fields.List(fields.String())

culinary_schema = CulinarySchema()
culinaries_schema = CulinarySchema(many=True)

# Culture Schema
class CultureSchema(ma.Schema):
    class Meta:
        fields = ['id', 'title', 'short_description', 'questions', 'answers', 'created_at', 'images', 'videos']

    questions = fields.List(fields.String())
    answers = fields.List(fields.String())

culture_schema = CultureSchema()
cultures_schema = CultureSchema(many=True)

# Media Schema
class MediaSchema(ma.Schema):
    class Meta:
        fields = ['id', 'media_type', 'media_url', 'description', 'blog_id', 'culinary_id', 'culture_id']

media_schema = MediaSchema()
medias_schema = MediaSchema(many=True)
