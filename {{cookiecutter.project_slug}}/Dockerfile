FROM python:3.11-slim


WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends

RUN python3 -m venv /opt/venv

COPY pyproject.toml ./

COPY {{cookiecutter.project_slug}}/ /app

RUN pip install .[dev]


{% if cookiecutter.create_jupyter_notebook == "yes"  %}

RUN python -m ipykernel install --user --name=venv
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

{% endif %}
