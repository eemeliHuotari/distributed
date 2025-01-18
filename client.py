import grpc
import test_pb2
import test_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(test_pb2.Operation(num1=10, num2=5))
        print(f"Addition Result: {response.result}")

if __name__ == '__main__':
    run()