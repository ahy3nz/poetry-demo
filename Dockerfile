FROM continuumio/miniconda3 AS build

RUN git clone https://github.com/ahy3nz/poetry-demo.git
WORKDIR /poetry-demo

RUN conda create -n poetry37 python=3.7 -yq && \
    . /opt/conda/etc/profile.d/conda.sh && \
    conda activate poetry37 &&\
    conda install -c conda-forge poetry -yq && \
    poetry install && \
    python -m pip install -e . && \
    echo "source activate poetry37" > ~/.bashrc


RUN chmod +x entrypoint.sh
ENTRYPOINT ["/poetry-demo/entrypoint.sh"]
