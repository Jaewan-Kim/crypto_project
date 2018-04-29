/**
 * MessageController
 *
 * @description :: Server-side logic for managing messages
 * @help        :: See http://sailsjs.org/#!/documentation/concepts/Controllers
 */

module.exports = {
	sendmessage: function(req,res){
		var email = req.param('senderemail',)
		var message = req.param('message',)

		var spawn = require("child_process").spawn;
		var pythonProcess = spawn('python',["smtp.py", email, message]);
		pythonProcess.stdout.on('data', function (data){
			console.log(data)
		});


	}
	
};

