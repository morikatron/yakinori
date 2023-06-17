# ベースとなるイメージを指定（この例では Python 3.8）
FROM python:3.8-slim-buster

# ワーキングディレクトリを設定
WORKDIR /app


RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y \
    build-essential \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    git \
    curl \
    xz-utils \
    make \
    file \
    unzip \
    sudo

# mecab-unidic-neologdをクローンし、インストール
RUN git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git \
    && cd mecab-unidic-neologd \
    && ./bin/install-mecab-unidic-neologd -n -y \
    && echo dicdir = `mecab-config --dicdir`"/mecab-unidic-neologd">/etc/mecabrc  \
    && sudo cp /etc/mecabrc /usr/local/etc \
    && cd .. \
    && rm -rf mecab-unidic-neologd

# 必要なライブラリをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# パッケージのソースコードをコピー
COPY . /app/

# パッケージをインストール
RUN python setup.py install
