from urllib import parse
import requests

import numpy as np
from flask import Flask, jsonify
from flask_cors import CORS

URL = 'http://127.0.0.1:5001'
URL2 = 'http://127.0.0.1:5005'


def RecommandationSystems():
    try:
        r = requests.get(parse.urljoin(URL, "get-all-stocks"))
        all_stocks = []
        for i in r.json()['message']:
            all_stocks.append(i['stock_symbol'])
        r = requests.get(parse.urljoin(URL2, "get-users-invest"))
        users_result = r.json()
        user_matrix = []
        for i in users_result:
            user_line = []
            print(i)
            for j in all_stocks:
                if j in users_result[i]:
                    print(str(users_result[i]) + str(users_result[i][j]))
                    user_line.append(users_result[i][j])
                else:
                    user_line.append(None)
            user_matrix.append(user_line)

        R = np.array(user_matrix)
        N = len(users_result)
        M = len(all_stocks)
        K = round(M / 2)

        nr_epoci = 1000
        alfa = 0.01
        U = np.random.rand(N, K)
        V = np.random.rand(K, M)

        epoca = 0
        while epoca < nr_epoci:
            MSE = []
            for n in range(0, N):
                for m in range(0, M):
                    if R[n][m] is not None:
                        for k in range(0, K):
                            s = 0
                            for z in range(0, K):
                                s = s + U[n][z] * V[z][m]
                            MSE_local = pow((R[n][m] - s), 2)
                            MSE.append(MSE_local)
            MSE = np.average(MSE)
            if MSE > 0.01:
                for n in range(0, N):
                    for m in range(0, M):
                        if R[n][m] is not None:

                            for k in range(0, K):
                                s = 0
                                for z in range(0, K):
                                    s = s + U[n][z] * V[z][m]

                                grU = (s - R[n][m]) * V[k][m]
                                grV = (s - R[n][m]) * U[n][k]
                                U[n][k] = U[n][k] - alfa * grU
                                V[k][m] = V[k][m] - alfa * grV
            else:
                break

            epoca = epoca + 1

        print('\nMatrice estimari')
        print(R)
        print('\n')

        rezultat = np.matmul(U, V)
        print(rezultat)
        users_list = list(users_result.keys())
        result = {}
        for i in range(0, len(rezultat)):
            list_of_rec = []
            x = np.argsort(rezultat[i])
            indexs = x[len(x) - 5:len(x)]
            for j in indexs:
                list_of_rec.append(all_stocks[j])
            result[users_list[i]] = list_of_rec

        print(result)
        return result
    except Exception as e:
        print(e)
        return None


application = Flask(__name__)
application.config['CORS_EXPOSE_HEADERS'] = 'Authorization'
application.config['CORS_ALLOW_HEADERS'] = ['Content-Type', 'Authorization']
application.config['CORS_ORIGINS'] = 'http://localhost:3000'
cors = CORS(application)


@application.route('/recommendation')
def recomandation_system():
    result = RecommandationSystems()
    if result is None:
        return jsonify({'message': 'No recommendation'}), 404
    else:
        return result, 200


if __name__ == "__main__":
    application.run(host='127.0.0.1', port=5006)
