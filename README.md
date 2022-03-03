# presigned-url-by-flask

## environment

```sh
python --version
  # Python 3.8.12
```

## getting started

```sh
pip install -r requirements.txt
```

## run

```sh
export AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
export AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
export BUCKET=${BUCKET}
export KEY=${KEY}

python handler.py
```

## make exe

```sh
pyinstaller handler.py --onefile
```

```sh
pyinstaller handler.spec
```
