from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


with open('README.md', 'r', encoding='utf-8') as fp:
    readme = fp.read()
long_description = readme
long_description_content_type = 'text/markdown'

setup(
    name='yakinori',
    version='0.1.1',
    url='https://github.com/morikatron/yakinori',
    author='Hikaru Yamada',
    author_email='hikaru.yamada@morikatron.co.jp',
    description='yakinori is a tool for converting Kanji to hiragana, katakana, roma-ji.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    license='MIT',
    keywords=['Japanese converter',
              'Japanese',
              'text preprocessing',
              'Hiragana',
              'Katakana',
              'Kanji',
              'alphabet'],
    python_requires='>=3.8',
    packages=find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
)
