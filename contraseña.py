import subprocess

def mostrar_contraseña():
    try:
        perfiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Output:", e.output.decode('utf-8'))
        return

    nombres_perfiles = []
    for i in perfiles:
        if "Perfil de todos" in i:
            i = i.split(":")
            nombres_perfiles.append(i[1].strip())

    for nombre_perfil in nombres_perfiles:
        try:
            resultado = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', nombre_perfil, 'key=clear']).decode('ISO-8859-1')
            contraseña = [linea.split(':')[1].strip() for linea in resultado.split('\n') if 'Contenido de la clave' in linea]
            print(nombre_perfil, contraseña)
        except subprocess.CalledProcessError as e:
            print(f"Error al obtener la contraseña para el perfil {nombre_perfil}: {e}")
            print("Output:", e.output.decode('ISO-8859-1'))

mostrar_contraseña()
