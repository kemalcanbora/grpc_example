var PROTO_PATH = __dirname + '/calculator.proto';

var grpc = require('grpc');
var hello_proto = grpc.load(PROTO_PATH);

var client = new hello_proto.Calculator('192.168.8.101:50051', grpc.credentials.createInsecure());

var response = client.SquareRootz({value:23784}, function(a, response) {console.log(response.value);});

