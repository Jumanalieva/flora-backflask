from flask import Blueprint, request, jsonify
from models import db, Culinary, Culture, Blog, Media, culinary_schema, culture_schema, blog_schema, blogs_schema

api = Blueprint('api', __name__, url_prefix='/api')

# Helper function to create an instance and commit to the database
def create_instance(model_class, schema, **kwargs):
    instance = model_class(**kwargs)
    db.session.add(instance)
    db.session.commit()
    return schema.dump(instance)

# CRUD for Culinary
@api.route('/culinary', methods=['POST'])
def create_culinary():
    title = request.json['title']
    short_description = request.json['short_description']
    questions = request.json.get('questions', [])
    answers = request.json.get('answers', [])
    images = request.json.get('images', [])
    videos = request.json.get('videos', [])
    return jsonify(create_instance(Culinary, culinary_schema, title=title, short_description=short_description, questions=questions, answers=answers, images=images, videos=videos))

@api.route('/culinary', methods=['GET'])
def get_all_culinary():
    culinary_items = Culinary.query.all()
    response = culinary_schema.dump(culinary_items, many=True)
    return jsonify(response)

@api.route('/culinary/<int:id>', methods=['GET'])
def get_single_culinary(id):
    culinary_item = Culinary.query.get(id)
    if not culinary_item:
        return jsonify({"error": "Culinary item not found"}), 404
    return jsonify(culinary_schema.dump(culinary_item))

@api.route('/culinary/<int:id>', methods=['PUT'])
def update_culinary(id):
    culinary = Culinary.query.get(id)
    if not culinary:
        return jsonify({"error": "Culinary item not found"}), 404
    culinary.title = request.json.get('title', culinary.title)
    culinary.short_description = request.json.get('short_description', culinary.short_description)
    culinary.questions = request.json.get('questions', culinary.questions)
    culinary.answers = request.json.get('answers', culinary.answers)
    culinary.images = request.json.get('images', culinary.images)
    culinary.videos = request.json.get('videos', culinary.videos)
    db.session.commit()
    return jsonify(culinary_schema.dump(culinary))

@api.route('/culinary/<int:id>', methods=['DELETE'])
def delete_culinary(id):
    culinary = Culinary.query.get(id)
    if not culinary:
        return jsonify({"error": "Culinary item not found"}), 404
    db.session.delete(culinary)
    db.session.commit()
    return jsonify(culinary_schema.dump(culinary))

# CRUD for Culture
@api.route('/culture', methods=['POST'])
def create_culture():
    title = request.json['title']
    short_description = request.json['short_description']
    questions = request.json.get('questions', [])
    answers = request.json.get('answers', [])
    images = request.json.get('images', [])
    videos = request.json.get('videos', [])
    return jsonify(create_instance(Culture, culture_schema, title=title, short_description=short_description, questions=questions, answers=answers, images=images, videos=videos))

@api.route('/culture', methods=['GET'])
def get_all_culture():
    cultural_items = Culture.query.all()
    response = culture_schema.dump(cultural_items, many=True)
    return jsonify(response)

@api.route('/culture/<int:id>', methods=['GET'])
def get_single_culture(id):
    culture_item = Culture.query.get(id)
    if not culture_item:
        return jsonify({"error": "Culture item not found"}), 404
    return jsonify(culture_schema.dump(culture_item))

@api.route('/culture/<int:id>', methods=['PUT'])
def update_culture(id):
    culture = Culture.query.get(id)
    if not culture:
        return jsonify({"error": "Culture item not found"}), 404
    culture.title = request.json.get('title', culture.title)
    culture.short_description = request.json.get('short_description', culture.short_description)
    culture.questions = request.json.get('questions', culture.questions)
    culture.answers = request.json.get('answers', culture.answers)
    culture.images = request.json.get('images', culture.images)
    culture.videos = request.json.get('videos', culture.videos)
    db.session.commit()
    return jsonify(culture_schema.dump(culture))

@api.route('/culture/<int:id>', methods=['DELETE'])
def delete_culture(id):
    culture = Culture.query.get(id)
    if not culture:
        return jsonify({"error": "Culture item not found"}), 404
    db.session.delete(culture)
    db.session.commit()
    return jsonify(culture_schema.dump(culture))

# CRUD for Blogs
@api.route('/blogs', methods=['POST'])
def create_blog():
    title = request.json['title']
    short_description = request.json['short_description']
    questions = request.json.get('questions', [])
    answers = request.json.get('answers', [])
    images = request.json.get('images', [])
    videos = request.json.get('videos', [])
    return jsonify(create_instance(Blog, blog_schema, title=title, short_description=short_description, questions=questions, answers=answers, images=images, videos=videos))

@api.route('/blogs', methods=['GET'])
def get_all_blogs():
    blogs = Blog.query.all()
    response = blogs_schema.dump(blogs)
    return jsonify(response)

@api.route('/blogs/<int:id>', methods=['GET'])
def get_single_blog(id):
    blog = Blog.query.get(id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404
    return jsonify(blog_schema.dump(blog))

@api.route('/blogs/<int:id>', methods=['PUT'])
def update_blog(id):
    blog = Blog.query.get(id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404
    blog.title = request.json.get('title', blog.title)
    blog.short_description = request.json.get('short_description', blog.short_description)
    blog.questions = request.json.get('questions', blog.questions)
    blog.answers = request.json.get('answers', blog.answers)
    blog.images = request.json.get('images', blog.images)
    blog.videos = request.json.get('videos', blog.videos)
    db.session.commit()
    return jsonify(blog_schema.dump(blog))

@api.route('/blogs/<int:id>', methods=['DELETE'])
def delete_blog(id):
    blog = Blog.query.get(id)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404
    db.session.delete(blog)
    db.session.commit()
    return jsonify(blog_schema.dump(blog))
