from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='yakinori',
    version='0.0.1',
    url='https://github.com/morikatron/yakinori',
    author='Hikaru Yamada',
    author_email='hikaru.yamada@morikatron.co.jp',
    description='yakinori is a tool for converting Kanji to hiragana, katakana, roma-ji.',
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
)
