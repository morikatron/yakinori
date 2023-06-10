# ベースとなるイメージを指定（この例では Python 3.8）
FROM python:3.8

# ワーキングディレクトリを設定
WORKDIR /app

# mecabとその依存関係をインストール
RUN apt-get update \
    && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    git 

# mecab-unidic-neologdをクローンし、インストール
RUN git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git \
    && cd mecab-unidic-neologd \
    && ./install-mecab-unidic-neologd -n -y \
    && echo dicdir = `mecab-config --dicdir`"/mecab-unidic-neologd">/etc/mecabrc && \
    && sudo cp /etc/mecabrc /usr/local/etc && \
    && cd .. \
    && rm -rf mecab-unidic-neologd

# 必要なライブラリをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# パッケージのソースコードをコピー
COPY . /app/

# パッケージをインストール
RUN python setup.py install
