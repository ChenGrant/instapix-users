import os
import sys
from concurrent import futures
from user_service import User
import grpc

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../proto")))
import user_pb2_grpc


# start grpc server
def start():
    server = grpc.server(futures.ThreadPoolExecutor())
    user_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port(f"{os.environ['DOMAIN']}:{os.environ['PORT']}")
    print("starting user server")
    server.start()
    server.wait_for_termination()
