from pb2 import calculator_pb2_grpc
from pb2 import calculator_pb2

import grpc

channel = grpc.insecure_channel('192.168.8.101:50051')

stub = calculator_pb2_grpc.CalculatorStub(channel)
number = calculator_pb2.Number(value=42)

response = stub.SquareRootz(number)

print(response.value)
