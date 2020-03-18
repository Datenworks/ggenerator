# GGenerator
[![Travis Build Status](https://travis-ci.org/Datenworks/ggenerator.svg?branch=master)](https://travis-ci.org/Datenworks/ggenerator)

## What is it? 

**GGenerator** is a command line interface that generates randomic data for tests purposes. It aims to be a easy client for programmers, data scientists, data analysts and data engineers to create a huge amount of data with a variety of complex data using JSON specification and a few commands on terminal.

## How to install

A easy way to install **ggenerator** cli is to use [pip](https://github.com/pypa/pip):

```bash
pip install ggenerator
```

After that you just have to learn how to use it.

## How to use it

If you do have a specification file, you just follow the next steps:

```bash
ggenerator generate --spec /file/path/example.json
```

If you dont, [click here]() and learn how to create a specification.


### MAC OS X Users
If you use MAC OS X, you need to setup two environment variables, for GGENERATOR be able to get your default language system
```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8 
```
## How to build it

You want to use the develop version or something like that?

Here you will have instruction of how to build this command line interface and have it ready for use.

The first thing you have to do is clone this repository:

```bash
git clone git@github.com:Datenworks/ggenerator.git
```

Now, you will need to create a virtualenv and install all the requirements. If you have [pipenv](https://github.com/pypa/pipenv) installed:

```bash
pipenv install --dev
```

If you dont have pipenv, you can learn how to install it by going to pipenv repository: https://github.com/pypa/pipenv

After that you can make your updates and fixes, so when you're ready execute:

```
pipenv run python setup.py build
pipenv run python setup.py install
```

Done, now you have built a new ggenerator client on your OS.

## License

[MIT](LICENSE)

## Contribute

We dont have it organized yet, but as soon as possible you will be able to contribute.