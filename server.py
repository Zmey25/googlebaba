from flask import Flask, request
from gradio_client import Client

app = Flask(__name__)
client = Client("ModularityAI/LLama3Chat")

@app.route('/')
def predict():
    message = request.args.get('message', default='', type=str)
    result = client.predict(
        message=message,
        request="You are helpful AI.",
        param_3=512,
        param_4=0,
        api_name="/chat"
    )
    return result

if __name__ == '__main__':
    app.run(debug=True)
