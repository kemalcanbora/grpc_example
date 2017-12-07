import grpc

from multiplication_example.pb2 import carpma_pb2_grpc
from multiplication_example.pb2 import carpma_pb2

channel = grpc.insecure_channel('192.168.8.101:50051')

stub = carpma_pb2_grpc.CalculatorStub(channel)
number = carpma_pb2.inputs(a=[4,2], b=5)

response = stub.carpma(number)

print(response.value)
