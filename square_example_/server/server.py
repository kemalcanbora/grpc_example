import time
from concurrent import futures

import grpc

from square_example.pb2 import calculator_pb2
from square_example.pb2 import calculator_pb2_grpc
from square_example.server import calculator


#python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):


    def SquareRootz(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)