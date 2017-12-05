from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

from model import ModelHandler

class WelcomeHandler(RequestHandler):
    def get(self):
        self.write("Welcome to our project page")

class PredictHandler(RequestHandler):
    def get(self):
        runtime = int(self.get_argument('runtime'))
        director = str(self.get_argument('director'))
        genre1 = str(self.get_argument('genre1'))
        genre2 = str(self.get_argument('genre2'))
        genre3 = str(self.get_argument('genre3'))

        ######### process in the modeling script?
        poster = str(self.get_argument('image_url'))

        ########### switch 'model.predict()' w/method call name equivalent to our model
        rating = self.application.model_handler.model.predict(runtime, director, genre1, genre2, genre3, poster)
        self.write('{}'.format(rating))

class ModelApplication(Application):
    def __init__(self, handler_mapping):
        self.model_handler = ModelHandler()
        super(ModelApplication, self).__init__(handler_mapping)



if __name__ == "__main__":
    handler_mapping = [
                       (r'/welcome', WelcomeHandler),
                       (r'/predict$', PredictHandler)                       
                      ]
    application = ModelApplication(handler_mapping)
    # application = Application(handler_mapping)
    application.listen(7777)
    IOLoop.current().start()