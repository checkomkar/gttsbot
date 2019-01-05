#!/bin/bash
cd /home/omkar/ga-sdk-source/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/grpc
python3 -m venv env
. env/bin/activate
python -m pushtotalk --device-id chatbot-223610 --device-model-id chatbot-223610-humanoidv1-q38rjh -i /home/omkar/gttsbot/output.wav
