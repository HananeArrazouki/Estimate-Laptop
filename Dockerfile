FROM python:3.8
RUN pip install pandas scikit-learn==1.2.2 streamlit
COPY src/app.py /app/
COPY csv/laptopPrice.csv /app/csv
COPY model/laptopPrice_model.pkl /app/model
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]