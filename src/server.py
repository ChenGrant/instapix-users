import os
import sys
from concurrent import futures
from user_service import User
import firebase
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../proto")))
import user_pb2_grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../config")))
from config import config_env


# start grpc server
def server():
    server = grpc.server(futures.ThreadPoolExecutor())
    user_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port(f"{os.environ['DOMAIN']}:{os.environ['PORT']}")
    print("starting user server")
    server.start()
    server.wait_for_termination()


def main():
    config_env()
    firebase.initialize()
    server()


if __name__ == "__main__":
    main()
