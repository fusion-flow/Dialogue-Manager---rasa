# Dialogue Manager - Rasa Core

In this project rasa core is trained to use as a dialogue manager. Intents, responses, and stories have defined relevant to the usecase. Following is the guidance to setup and run the trained rasa core. This is build to get the generated response when intent is given.

## Dialogue Manager Setup

* Clone the code of dialogue manager from [https://github.com/fusion-flow/Dialogue-Manager---rasa.git](https://github.com/fusion-flow/Dialogue-Manager---rasa.git).
* Create a virtual environment to run the code. (Python version=3.9.12).
* Install rasa
      `pip install rasa`
* Train rasa core
      `rasa train core`
* A trained rasa core model will be created in models directory. Change that model name to core.tar.gz in order to match with the Dockerfile.
* Build the docker image.
      `docker build -t rasa-core .`
* Run the docker image.
      `docker run -p 8080:8080 rasa-core`
* Now you can call the api by sending post requests to http://localhost:8080/webhooks/rest/webhook and content should be in { "sender": "1", "message": "/greet"} format. And it will return the corresponding response.
