var http = require('http');
var myPythonScriptPath = 'main_output.py';

// Use python shell
var PythonShell = require('python-shell');
var pyshell = new PythonShell(myPythonScriptPath);

var changed = 0;
var text = ""
var strings = '';

pyshell.on('message', function (message) {
    // received a message sent from the Python script (a simple "print" statement)
	console.log(message)
    a = message.split(';')
    //string1 = a[1].split(':')[1]
	//string0 = a[0].split(':')[1]
	//strings = string0 + string1 
	//strings=message
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

          res.end(strings)



    }).listen(8002);

    console.log('finished');
});
