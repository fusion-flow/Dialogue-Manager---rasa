# Dialogue Manager - Rasa Core

In this project rasa core is trained to use as a dialogue manager. Intents, responses, and stories have defined relevant to the usecase. Following is the guidance to setup and run the trained rasa core. This is build to get the generated response when intent is given.

## Dialogue Manager Setup

* Clone the code of dialogue manager from [https://github.com/fusion-flow/Dialogue-Manager---rasa.git](https://github.com/fusion-flow/Dialogue-Manager---rasa.git).
* Create a virtual environment to run the code. (Python version=3.9.12).
* Install rasa
      ```
         pip install rasa
      ```
* Train rasa core
      ```
        rasa train core
      ```
* A trained rasa core model will be created in models directory. Change that model name to core.tar.gz in order to match with the Dockerfile.
* You can locally run model using the following command.
      ```rasa run --model models/core.tar.gz --enable-api```
* Or you can build and run the docker image using following commands.
* Build the docker image.
      ```docker build -t rasa-core .```
* Run the docker image.
      ```docker run -p 8080:8080 rasa-core```
* Then you can call use the following CURL command to send an intent to generate the response.
    `curl --location 'http://localhost:8080/webhooks/rest/webhook' \
       --header 'Content-Type: application/json' \
       --data '{
            "message": "/confirm"
       }'`

## Acknowledgement

We would like to acknowledge the following repository of Rasa framework that used for the implementation of this project.

- [Rasa](https://github.com/RasaHQ/rasa)

The original work is licensed under the [Apache v2 license](http://www.apache.org/licenses/LICENSE-2.0)

