FROM apify/actor-python:3.9

COPY requirements.txt ./

RUN echo "Python version:" \
    && python --version \
    && echo "Pip version:" \
    && pip --version \
    && echo "Installing dependencies:" \
    && pip install -r requirements.txt \
    && echo "All installed Python packages:" \
    && pip freeze

COPY . ./

RUN python -m compileall -q .

CMD ["python", "-m", "src"]