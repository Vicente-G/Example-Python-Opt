# Example-Python-Opt

[![tests](https://github.com/Vicente-G/Example-Python-Opt/actions/workflows/ci.yml/badge.svg?event=pull_request)](https://github.com/Vicente-G/Example-Python-Opt/actions/workflows/ci.yml)
[![deploy](https://github.com/Vicente-G/Example-Python-Opt/actions/workflows/cd.yml/badge.svg?event=push)](https://github.com/Vicente-G/Example-Python-Opt/actions/workflows/cd.yml)
[![license](https://img.shields.io/badge/license-MIT-purple.svg)](https://github.com/Vicente-G/Database-Model/blob/main/LICENSE)

This is an example of service written in `Python`, it provides a base from which make other services. The implementation uses `gunicorn`, `Flask`

## Installation

To run this service locally, you require `Python` which can be downloaded [here](https://www.python.org/downloads/) and you may require the `Docker` daemon as well, which can be easily installed with [Docker Desktop](https://www.docker.com/products/docker-desktop/). However, if you plan to run this service on the cloud, the best way is to fork this repo and edit the `cd.yml` file to deploy it with Continous Deployment. (CD) Also, after forking you can set the CD with your provider, it must be possible for sure.

Following the local installation, run the following commands in order:

```sh
git clone https://github.com/Vicente-G/Example-Python-Opt
cd example-python-opt
```

Now you should be on the service folder, from where you can run it with either `Python` or `Docker`, depending on your needs.

## Running

If you plan on editing this service to your needs, you may prefer `Flask`, as it can be continously tested with its debug mode. To run this example using `Python`, install the dependencies and run the `dev` script, like this:

```sh
pip install --user pdm
pdm sync
pdm run dev
```

In the other hand, if you plan to just run the service in your local server, the best option is to use containers, for reliability and security. With that on mind, `Docker` is your option. First enable the Docker daemon, and right after run these commands:

```sh
docker build -t example-python-opt .
docker run -p 8080:8080 -e PORT='8080' example-python-opt
```

In any way you run the service, it will block your terminal. Now, to test its responses, you can try any HTTP request emitter, such as Postman, Axios or cURL. The following example shows a GET request over the service with cURL

```sh
curl --head localhost:8080/status
```

If everything is working as intended, the answer to that response should be a 200, which means that everything is okay! (The 200 should be in the first line or so)

## Requests

As this is just an example, this service only has one extra route asides from the `status` one. This service provides the route `example`, with the following command:

```sh
curl localhost:8080/example
```

The output should be something with this shape:

```json
{
    "hello": "world"
}
```
