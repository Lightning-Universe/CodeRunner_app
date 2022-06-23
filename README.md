## Demo

Latest demo: https://01g685vn5feeappfbtvncnpjyh.litng-ai-03.litng.ai/view/React%20UI

## Milestone v0.1 Tracker

All the issues are tracked here: https://github.com/Lightning-AI/Code-Editor-App/issues/1.

## Goal

Here is how the initial goal for this app looked like:

1. One work will have the editor running, they'll have a template with a class method having an input as a frame coming from the webcam -- they are free to play around with it, write the code, and return the modified frame.
2. Click submit, and demo!
3. It can be served with gradio - and the next tab will show the input video, as well as the output video frame by frame.

Might change with time. :)

## Running (locally/cloud)

```bash
git clone git@github.com:Lightning-AI/LAI-CodeRunner-App.git && cd LAI-CodeRunner-App
pip install lightning
# Locally
lightning run app app.py
# Cloud
lightning run app app.py --cloud
```

## Development (Building)

```bash
git clone git@github.com:Lightning-AI/LAI-CodeRunner-App.git && cd LAI-CodeRunner-App
pip install lightning
cd ui/ && yarn install && yarn build
# To just test the UI:
yarn start
# And open localhost:8080
# Else just run the app
cd ../ && lightning run app app.py
```

