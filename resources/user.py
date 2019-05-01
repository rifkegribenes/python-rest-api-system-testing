from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!")

    def post(self, username, password):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "A user with username '{}' already exists.".format(username)}, 400

        user = UserModel(username, **data)

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred inserting the user."}, 500

        return {"message": "User created successfully"}, 201