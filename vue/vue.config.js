module.exports = {
	devServer : {
		proxy : {
			'/api' : {
				target       : 'http://python-api:5000',
				changeOrigin : true,
				logLevel     : 'debug'
			}
		}
	}
};