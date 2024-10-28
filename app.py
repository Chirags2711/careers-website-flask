from flask import Flask
# from module import class

app = Flask(__name__) #an object of class Flask
# print(__name__) # prints name. inside python script, this var is already present. It will refer, corresponding to how this name was invoked

#Create a route. When URL path is accessed, run hello_world
@app.route("/")
def hello_world():
  return "Hello World"

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True) # debug true for auto changes