from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc

class CalculatorService(test_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return test_pb2.Result(result=request.num1 + request.num2)
    
    def Subtract(self, request, context):
        return test_pb2.Result(result=request.num1 - request.num2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()