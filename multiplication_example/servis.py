import time
from concurrent import futures

import grpc
import multiplication_example.carpma as carpma

from multiplication_example.pb2 import carpma_pb2
from multiplication_example.pb2 import carpma_pb2_grpc

class CalculatorServicer(carpma_pb2_grpc.CalculatorServicer):

    def carpma(self, input, context):
        print(type(input.a))
        print(input.a[0])
        print(type(input.a[0]))

        response = carpma_pb2.return_x(value=carpma.carpma(list(input.a),input.b))

        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
carpma_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

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