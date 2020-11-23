from flask import Flask, request, make_response, redirect
#Se crea un objeto del tipo app
app = Flask (__name__)

@app.route('/')
def homeRoute():
    user_ip = request.remote_addr
    response = make_response (redirect('Hello'))
    response.set_cookie('ip',user_ip)
    response.set_cookie('Perro', 'Bruno')
    return response
@app.route('/Hello')
def helloRoute():
    return 'Hola todo anda bien'

if __name__ == '__main__':
    app.run()
