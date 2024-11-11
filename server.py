import grpc
from concurrent import futures
import example_pb2
import example_pb2_grpc

class MathService(example_pb2_grpc.MathServiceServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return example_pb2.AddResponse(result=result)

    def Multiply(self, request, context):
        result = request.a * request.b
        return example_pb2.MultiplyResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_MathServiceServicer_to_server(MathService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
