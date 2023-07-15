import os
import sys
from firebase_admin import auth
from firebase_admin._auth_utils import InvalidIdTokenError

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../proto")))
import user_pb2
import user_pb2_grpc


class User(user_pb2_grpc.UserServicer):
    def AuthenticateUser(self, request, context):
        print("AuthenticateUser request received")
        try:
            decoded_token = auth.verify_id_token(request.firebase_id_token)
            uid = decoded_token["uid"]
        except InvalidIdTokenError:
            uid = ""
        return user_pb2.AuthenticateUserResponse(uid=uid)
