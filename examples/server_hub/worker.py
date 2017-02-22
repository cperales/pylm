from pylm.servers import Worker
import sys


class MyWorker(Worker):
    def foo(self, message):
        self.logger.info('Processed')
        return self.name.encode('utf-8') + b' processed ' + message

server = MyWorker(sys.argv[1], 'tcp://127.0.0.1:5561')

if __name__ == '__main__':
    server.start()