import grpc
import calculator_pb2
import calculator_pb2_grpc
 
def run():
      with grpc.insecure_channel('3.17.172.30:50051') as channel:

        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'La suma de los numeros es : {response.result}')

        response = stub.Subtract(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'La resta de los numeros es: {response.result}')

        response = stub.Multiply(calculator_pb2.OperationRequest(a=10, b=5))
        print(f'La multiplicacion de los numeros es: {response.result}')

        response = stub.Divide(calculator_pb2.OperationRequest(a=10, b=1))
        print(f'La divicion de los numeros es: {response.result}')

if __name__ == '__main__':
    run()