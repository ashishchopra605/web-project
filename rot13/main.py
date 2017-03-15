import os

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

def rot13(text):
    str = ""
    for i in range(0,len(text)):
        if text[i].isalpha():
           if text[i].islower():
              if((ord(text[i]) + 13) > 96) and ((ord(text[i]) + 13) < 123):
                  str += chr(ord(text[i]) + 13)
              else:
                 if((ord(text[i]) - 13) > 96) and ((ord(text[i]) - 13) < 123):
                     str += chr(ord(text[i]) - 13)
           else:
              if text[i].isupper():
                 if((ord(text[i]) + 13) > 64) and ((ord(text[i]) + 13) < 91):
                     str += chr(ord(text[i]) + 13)
                 else:
                     if text[i].upper() and ((ord(text[i]) - 13) > 64) and ((ord(text[i]) - 13) < 91):
                        str += chr(ord(text[i]) - 13)  
        else:
           str += text[i] 
    return str 

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
      
    def render(self, template , **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        rot = self.request.get('text')
        text = rot13(rot)
        self.render("rot13.html",text = text)

    def post(self):
        rot = self.request.get('text')
        text = rot13(rot)
        self.render("rot13.html",text = text)
       

app = webapp2.WSGIApplication([('/',MainPage)],debug = True)
