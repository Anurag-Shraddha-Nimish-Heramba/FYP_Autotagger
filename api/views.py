from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import numpy as np
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response

import tensorflow
# Create your views here.
@api_view(['POST'])
def apiOverview(request):
    # print("Hello")
    loaded_model = tensorflow.keras.models.load_model("model_15k")
    
    with open('filename.pkl', 'rb') as handle:
        most_common = pickle.load(handle)

    temp = []
    for word in most_common: # iterating each most common word for each issue
        if word[0] not in request.data['issue']:
            temp.append(0)
        else:
            temp.append(1)
    
    res_index = []

    result = loaded_model.predict(np.array([temp,]))

    for i in range(3):
        res_index.append(np.argmax(result))
        result[0][np.argmax(result)] = 0

    tag_map = {0: 'Credit reporting, credit repair services, or other personal consumer reports', 1: 'Debt collection', 2: 'Mortgage', 3: 'Vehicle loan or lease', 4: 'Credit card or prepaid card', 5: 'Payday loan, title loan, or personal loan', 6: 'Money transfer, virtual currency, or money service', 7: 'Checking or savings account', 8: 'Student loan'}
    res_tags = [tag_map[res] for res in res_index]

    return JsonResponse({"res": res_tags})