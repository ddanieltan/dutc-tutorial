#!/usr/bin/env python3
from flask import Flask, request, jsonify
from algorithm import approx

app=Flask(__name__)

@app.route('/')
def put_task():
    f=request.json['f']
    a=request.json['a']
    b=request.json['b']
    c=request.json['c']
    d=request.json['d']
    size=request.json.get('size',100)

    response = {
        'result': approx(f,a,b,c,d,size),
    }
    return jsonify(response)

if __name__=='__main__':
    app.run(debug=True)
    # http calls httpie package
    # usage ->  http GET http://localhost:5000 f='sqrt(4 - xs**2)' a:=0 b:=2 c:=0 d:=2