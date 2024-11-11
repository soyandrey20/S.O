import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
      with grpc.insecure_channel('3.17.172.30:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'Add: {response.result}')
        response = stub.Subtract(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'Subtract: {response.result}')
        response = stub.Multiply(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'Multiply: {response.result}')
        response = stub.Divide(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'Divide: {response.result}')

if __name__ == '__main__':
    run()