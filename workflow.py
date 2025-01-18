from fastapi import FastAPI
from kafka import KafkaProducer
import grpc
import test_pb2
import test_pb2_grpc

app = FastAPI()

producer = KafkaProducer(bootstrap_servers='localhost:9092')

@app.post("/calculate-and-notify/")
async def calculate_and_notify(num1: float, num2: float):

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(test_pb2.Operation(num1=num1, num2=num2))
    

    producer.send('notifications', f"Calculation result: {response.result}".encode())
    producer.flush()
    
    return {"result": response.result}