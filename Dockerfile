FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /home/appuser/app

COPY . .

ENV STREAMLIT_BROWSER_GATHERUSAGESTATS=false
ENV STREAMLIT_CONFIG_DIR=/home/appuser/.streamlit
ENV MEM0_DIR=/home/appuser/.mem0
ENV EMBEDCHAIN_DIR=/home/appuser/.embedchain

RUN mkdir -p $STREAMLIT_CONFIG_DIR $MEM0_DIR $EMBEDCHAIN_DIR && \
    chmod -R 777 /home/appuser && \
    pip install --no-cache-dir -r requirements.txt

USER appuser

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]

