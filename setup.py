from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A desktop assistant for your windows'
LONG_DESCRIPTION = 'A package that make your daily stuff easier than ever'

# Setting up
setup(
    name="Grace_nn",
    version=VERSION,
    author="QuickCodes (Dhruv Soni)",
    author_email="<dhruvcodes7220@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="",
    packages=find_packages(),
    install_requires=['pytorch', 'jsons', 'wikipedia', 'pywhatkit', 'nltk', 'requests', 'webbrowser', 'pyttsx3',
                      'speech', 'speech_recognition', 'numpy'],
    keywords=['python', 'stream', 'Neural network assistant', 'virtual assistant', 'desktop assistant', 'artificial assistant'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)