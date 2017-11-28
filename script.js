var http = require('http');
var myPythonScriptPath = 'script.py';

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

      document.getElementById('this').innerHTML = word
    };
    http.createServer(function (req, res) {
      console.log('request received');
      if (req['url'][6]=='1'){
        console.log('request received');
        res.writeHead(200, {'Content-Type': 'text/plain'});
        if (changed == 0){
                  res.end(strings.join())
        }
        else if (changed == 1) {
          res.end(text)
        }}
      else{
        console.log(
        )
        text = req['url']
        changed = 1
        console.log(text)
      }
    }).listen(8001);

    console.log('finished');
});
