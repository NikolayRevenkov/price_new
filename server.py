
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import scipy.sparse as sp
import numpy as np

#загружаем сохраненные модель, кодировщик и скаляр из файла pkl    
with open('C:\Final_Project\model_and_encoders_and_scaler.pkl', 'rb') as f:
    xgb_random, encoder, scaler = pickle.load(f)
    
#Запускаем обработчик запросов    
app = Flask(__name__)
@app.route('/add', methods=['POST'])
def add():
    #получаем данные
    data=request.json
    propertyType=data.get('propertyType')
    state=data.get('state')
    status=data.get('status')
    bath_new=data.get('bath_new')
    beds_new=data.get('beds_new')
    sqft_new=data.get('sqft_new')
    Total_Population=data.get('Total Population')
    year_new=data.get('year_new')
    sc_ra=data.get('sc_ra')
    sc_di=data.get('sc_di')
    
    #собираем их в DataFrame
    d = {'propertyType': propertyType, 'state': state,'status':status,'bath_new':bath_new,'beds_new':beds_new,'sqft_new':sqft_new,'Total Population':Total_Population,'year_new':year_new,'sc_ra':sc_ra,'sc_di':sc_di}
    data=pd.DataFrame(data=d, index=[0])
    
    #кодируем, стандартизируем
    X_test_enc=encoder.transform(data[['state','propertyType','status']])
    X_test_scaler=scaler.transform(data[['bath_new','beds_new','sqft_new','Total Population','year_new','sc_ra','sc_di']])
    X_test = sp.hstack((X_test_enc, X_test_scaler))
    #запускаем модель и делаем предсказание
    y_predict=np.exp(xgb_random.predict(X_test))
    
    y_df=pd.DataFrame(y_predict,columns=['Predicted price'])
    data_json=y_df.to_json(orient='records')
    # Преобразование DataFrame в HTML-таблицу
    y_df.to_csv('zhopa_predict.csv',index=False)
    #вовзаращаем предсказание стоимости
    return jsonify(data_json)


if __name__ == '__main__':

    app.run('localhost', 5000)


