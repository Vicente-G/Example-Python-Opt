FROM python:3.9-slim
WORKDIR /server
RUN pip install -U pip setuptools wheel
RUN pip install pdm
COPY pyproject.toml pdm.lock LICENSE README.md ./
COPY src/ ./src
RUN mkdir __pypackages__ && pdm sync --prod --no-editable
CMD pdm run start
