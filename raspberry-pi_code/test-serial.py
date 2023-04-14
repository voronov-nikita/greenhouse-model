from flask import Flask, jsonify
import serial

# порт для Raspberry pi 3
PORT = "/dev/ttyACM0"

app = Flask(__name__)


@app.route('/')
def index():
    return {"Hello": "world"}


# <---------------- Температуры и влажности воздуха --------------->
@app.route('/temp_hum/1')
def index1():
    pin = 2
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'22')
    # data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(0),
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/temp_hum/2')
def index2():
    pin = 3
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'23')
    # data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(0),
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/temp_hum/3')
def index3():
    pin = 4
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'24')
    # data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(0),
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/temp_hum/4')
def index4():
    pin = 5
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'25')
    # data_value = ser.readline().decode('utf-8').split()
    data = {
        'pin': pin,
        'temperature': float(0),
        'humidity': float(0)
    }
    return jsonify(data)


# <---------------- Почва --------------->

@app.route('/hum/1')
def index5():
    pin = 7
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'17')
    # data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/hum/2')
def index6():
    pin = 8
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'18')
    # data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/hum/3')
def index7():
    pin = 9
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'19')
    # data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/hum/4')
def index8():
    pin = 10
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'110')
    # data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/hum/5')
def index9():
    pin = 11
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'111')
    # data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(0)
    }
    return jsonify(data)


@app.route('/hum/6')
def index10():
    pin = 12
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b'112')
    # data_value = ser.readline().decode('utf-8')
    data = {
        'pin': pin,
        'humidity': float(0)
    }
    return jsonify(data)


# <---------------- Сервопривод --------------->
@app.route('/fork_drive/')
def index11():
    # ser = serial.Serial(PORT, 9600)
    # ser.write(b"3")
    return "True"


# старт сервера
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

