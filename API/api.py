# import flask
# from flask_restplus import Resource, Api
# from flask import request, jsonify
#
# from database.session_repository import InMemoryRepository
#
# app = flask.Flask(__name__)
# api = Api(app)
#
# repository = InMemoryRepository()
#
# # Resources
# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return jsonify(repository.read_all())
#
# @api.route('/api/v1/sessions')
# class Session(Resource):
#
#     def get(self):
#         if 'id' in request.args:
#             return jsonify(repository.read(request.args['id']))
#         return jsonify(repository.read_all())
#
# # @app.route('/api/v1/sessions', methods=['POST'])
# # def post():
# #     if 'id' in request.args:
# #         body = request.json
# #     return jsonify(repository.read_all())
#
# if __name__ == '__main__':
#     app.run(debug=True)