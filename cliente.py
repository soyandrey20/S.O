import grpc
import example_pb2
import example_pb2_grpc

def run():
    with grpc.insecure_channel('18.223.101.78:50051') as channel:

        stub = example_pb2_grpc.MathServiceStub(channel)
        
        response = stub.Add(example_pb2.AddRequest(a=5, b=10))
        print("Addition Result:", response.result)
        
        response = stub.Multiply(example_pb2.MultiplyRequest(a=5, b=10))
        print("Multiplication Result:", response.result)

if __name__ == '__main__':
    run()
