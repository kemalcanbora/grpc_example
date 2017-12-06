from pb2 import calculator_pb2_grpc
from pb2 import calculator_pb2

import grpc

channel = grpc.insecure_channel('localhost:50051')

stub = calculator_pb2_grpc.CalculatorStub(channel)
number = calculator_pb2.Number(value=16)

response = stub.SquareRootz(number)

print(response.value)
