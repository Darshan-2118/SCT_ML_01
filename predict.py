import joblib
import numpy as np
import pandas as pd

# Load saved artifacts
model    = joblib.load('model/model.pkl')
scaler   = joblib.load('model/scaler.pkl')
features = joblib.load('model/features.pkl')

def predict_price(gr_liv_area, total_bsmt_sf, first_flr_sf, second_flr_sf,
                  bedrooms, full_bath, half_bath, bsmt_full_bath, tot_rms):

    sample = pd.DataFrame([{
        'GrLivArea'   : gr_liv_area,
        'TotalBsmtSF' : total_bsmt_sf,
        '1stFlrSF'    : first_flr_sf,
        '2ndFlrSF'    : second_flr_sf,
        'BedroomAbvGr': bedrooms,
        'FullBath'    : full_bath,
        'HalfBath'    : half_bath,
        'BsmtFullBath': bsmt_full_bath,
        'TotRmsAbvGrd': tot_rms,
        'TotalSqFt'   : gr_liv_area + total_bsmt_sf,
        'TotalBaths'  : full_bath + 0.5 * half_bath + bsmt_full_bath
    }])

    log_pred = model.predict(scaler.transform(sample[features]))
    return np.expm1(log_pred)[0]


if __name__ == '__main__':
    print(' House Price Predictor')
    print('-' * 30)

    gr_liv_area    = float(input('Above-grade living area (sq ft): '))
    total_bsmt_sf  = float(input('Basement area (sq ft, 0 if none): '))
    first_flr_sf   = float(input('First floor (sq ft): '))
    second_flr_sf  = float(input('Second floor (sq ft, 0 if none): '))
    bedrooms       = int(input('Number of bedrooms: '))
    full_bath      = int(input('Full bathrooms: '))
    half_bath      = int(input('Half bathrooms: '))
    bsmt_full_bath = int(input('Basement full bathrooms: '))
    tot_rms        = int(input('Total rooms above grade: '))

    price = predict_price(gr_liv_area, total_bsmt_sf, first_flr_sf, second_flr_sf,
                          bedrooms, full_bath, half_bath, bsmt_full_bath, tot_rms)

    print(f'\nThe Predicted Sale Price: ${price:,.0f}')