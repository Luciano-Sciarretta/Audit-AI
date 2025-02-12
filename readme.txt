Iniciar la aplicación:

1. Activar el entorno virtual
Navegar a la carpeta del entorno virtual y activarlo:

En Windows (CMD o PowerShell): cd VENV/Scripts/activate

2. Ir al directorio del proyecto
Retroceder dos niveles hasta el directorio raíz de la aplicación:

cd ../..

3. Crear la base de datos y opcional un superusuario para poder usar el admin panel(hay acceso directo en la navbar) de django.

    Crear la base de datos: 
        python manage.py makemigrations
        python manage.py migrate

    Super usuario:
        python manage.py createsuperuser

    Inciar la aplicación:
        python manage.py runserver

3. Ejecutar el servidor de desarrollo
Ejecutar el siguiente comando en la raíz del proyecto:

python manage.py runserver

4. Copiar o darle click con ctrl presionado al número de puerto para abrir la app.









