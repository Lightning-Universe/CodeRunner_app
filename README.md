## Features added

1. Monaco Editor integration (referred from: https://github.com/microsoft/monaco-editor/tree/main/samples/browser-esm-webpack-typescript-react)
2. Theme: dark by default (`vs-dark`)
3. Language: Python

## Running (locally/cloud)

```bash
git clone <> && cd <>
pip install lightning
# Locally
lightning run app app.py
# Cloud
lightning run app app.py --cloud
```

## Development (Building)

```bash
git clone <> && cd <>
pip install lightning
cd ui/ && yarn install && yarn build
# To just test the UI:
yarn start
# And open localhost:8080
# Else just run the app
cd ../ && lightning run app app.py
```

