import eventlet
import json
from eventlet import wsgi


def serve(env, start_response):
	if env['PATH_INFO'] != '/':
		start_response('404 Not Found', [('Content-Type', 'text/plain')])
		return ['Not found']

	start_response('200 OK', [('Content-Type', 'application/json')])
	f = open()
	response = json.dumps({'tweets': 'hello world'})
	return [response]


if __name__ == '__main__':
	wsgi.server(eventlet.listen(('127.0.0.1', 8090)), serve)

