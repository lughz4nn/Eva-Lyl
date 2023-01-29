# Eva-Lyl
Programa para consultar el nombre de institución, id y permisos de administrador de un documento o e-mail registrado el la plataforma eva.lyl.com/#/principal

## Instalación
```console
$ git clone https://github.com/lughz4nn/Eva-Lyl
$ cd Eva-Lyl
$ pip3 install -r requirements.txt
```

## Uso
```console
$ python3 main.py <documento o email> <accion [consultar,atacar]>
# La opción atacar (fuerza bruta) se implementará en el futuro
```

## Ejemplo
```console
# Esto hará una consulta hacía el correo "juan@gmail.com"
$ python3 main.py juan@gmail.com consultar

# Esto hará una consulta hacía al npumero de documento "1043443322"
$ python3 main.py 1043443322 consultar
```

## Actualizar
```console
# Primero accede al directorio eva-lyl
$ git pull
```

<br/>

<footer style="text-align: center;">
    <strong><i>No me hago responsable del mal uso del programa.</i></strong>
</footer>
