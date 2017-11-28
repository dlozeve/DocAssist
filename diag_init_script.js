var http = require('http');
var myPythonScriptPath = 'healthrecord/speech2text.py';

// Use python shell
var PythonShell = require('python-shell');
var pyshell = new PythonShell(myPythonScriptPath);

var changed = 0;
var text = ""
var strings = [];

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)

    strings.push(message)
});

// end the input stream and allow the process to exit
pyshell.end(function (err) {
    if (err){
        throw err;


    };
    http.createServer(function (req, res) {
      console.log('request received');

        console.log('request received');
        res.writeHead(200, {'Content-Type': 'text/plain'});

          res.end(strings.join())



    }).listen(8003);

    console.log('finished');
});
