# Ejercico N1

# se cree una lista vacia
Numero =[]
# Se determina variable N
N = 1
# Se indica que el bucle 
while N >= 0:
    # Se le pide al usuario ingresar un numero
    N = int(input("Ingrese un numero"))
    # Si el numero es mayor a 0 imprimir
    if N >= 0:
        Numero.append(N)
# Si el numero es menor a 0 (-1) termina el bucle y no incluye el numero negativo o menor
print(Numero)
 


# Ejercicio 2

# Se crean listas vacia
lista1 = []
lista2 = []
lista3 = []
# Se utuliza for para determinar los bubles, pidiendole al usuario ingresar un numero (maximo 5) en cada lista
for indice in range(1,6):
	lista1.append(int(input("Introduce el elemento %d del vector1:" % indice)))
for indice in range(1,6):
	lista2.append(int(input("Introduce el elemento %d del vector2:" % indice)))
# Crea a lista 3 sumando la lista 1 y la lista 2
for indice in range(0,5):
	lista3.append(lista1[indice] + lista2[indice])

print("La suma de los vectores es:")
for numero in lista3:
	print(numero," ",end="")


# Ejercico 3

# Se define la funcion
def main():
    #Se crea una lista vacia
    temperaturas = []
    # Se crea un bucle donde se solicita la temperatura de 5 dias 
    for i in range(1, 6):
        # Se le pide que por cada dia cumpla unas condiciones
        print(f"\nDía {i}:")
        while True:
            try:
                # Ingresa la temperatura minima
                min_temp = float(input("Ingrese la temperatura mínima: "))
                # Ingresa la temperatura maxima
                max_temp = float(input("Ingrese la temperatura máxima: "))

				# Valida que la temperatina minima no sea mayor a la temperatura maxima
                if min_temp > max_temp:
                    print("Error: La temperatura mínima no puede ser mayor que la máxima")
                    continue
				# Los datos se almacenan en la lista de temperatura
                temperaturas.append({
                    "dia": i,
                    "min": min_temp,
                    "max": max_temp})
                break
            # Si no se ingresa un numero si no valor de texto imprime el siguiente un mensaje avisando el error
            except ValueError:
                print("Error: Por favor ingrese un número válido para la temperatura")
                            
    print("\nTemperatura media por día:")
    for dia in temperaturas:
        # Calcula media de la temperatu sumando la temperatura minima y la maxima diviendola en 2
        media = (dia["min"] + dia["max"]) / 2
        # Se le pide que imprima la temperatura con formato .2f
        print(f"Día {dia['dia']}: {media:.2f}°C")

	# Se usa para determinar la temperatura minima general
    menor_temp = min(dia['min'] for dia in temperaturas) 

    print("\nDías con la menor temperatura:")
    dias_menor_temp = [dia["dia"] for dia in temperaturas if dia["min"] == menor_temp]
    if dias_menor_temp:
        for dia in dias_menor_temp:
            print(f"Día {dia} con {menor_temp}°C")
    else:
        print("No hay días registrados.")
        
    # Se usa para buscar la temperatura maxima en los dias registrados
    try:
        temp_buscar = float(input("\nIngrese una temperatura para buscar días con esa máxima: "))
        dias_coincidentes = [dia["dia"] for dia in temperaturas if dia["max"] == temp_buscar]
        if dias_coincidentes:
            print(f"Días con temperatura máxima de {temp_buscar}°C:")
            for dia in dias_coincidentes:
                print(f"Día {dia}")
        # En caso de que la temperatura no coincida imprima
        else:
            print(f"No hay días con temperatura máxima de {temp_buscar}°C.")
    except ValueError:
        print("Error: Temperatura no válida.")

if __name__ == "__main__":
    main()
       
# Ejercicio 4

# Se importa la biblioteca random
import random

# Se le pide generar un numero aleatorio en 1 y 100 
aleatorio= random.randint(1,100)

# Se crea el bucle
while True:
     # Se pide ingresar un numero
     num=int(input("Ingrese un numero entre 1 y 100"))
     # Si adivina el numero imprima el mensaje y finaliza el juego
     if num == aleatorio:
          print("Felicidades adivinaste el numero")
          break
     # Avisa si el numero es mayor
     elif num < aleatorio:
          print("El numero es mayor intenta nuevamente")
     # Avisa si el numero es menor
     elif num > aleatorio:
          print("El numero es menor intenta nuevamente")
# Anuncia la finalizacion del juego        
print("Fin del Juego")

# Ejercicio 5

#importar las bibliotecas
import tweepy
import pandas as pd

def authenticate():
    # Credenciales de la API (X)
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAJxc0gEAAAAAjLk8ZAN5Voa7ozQzfaEsCFOeNZc%3DAcyZ3XojxV0KxQLJAlWQQiQGyNvjyIuB20nUc5hgfqwCM1ayN1"
    try:
        client = tweepy.Client(bearer_token=bearer_token)
        print("Autenticación exitosa. Puedes continuar.")
        return client
    except Exception as e:
        print(f"Error en la autenticación: {e}")
        return None

def get_user_list(num_users):
    "Obtiene la lista de usuarios a analizar"
    user_list = []
    for i in range(num_users):
        username = input(f"Por favor introduce el nombre de usuario #{i+1} (con o sin @): ").strip()
        user_list.append(username.lstrip("@"))
    return user_list

def analyze_tweets(api_client, user_list):
    "Analiza los tweets de los usuarios proporcionados"
    tweet_data = []
    
    for username in user_list:
        try:
            # Obtener información del usuario
            user = api_client.get_user(username=username)
            if not user.data:
                print(f"Usuario @{username} no encontrado")
                continue
                
            user_id = user.data.id
            
            # Obtener tweets del usuario
            tweets = api_client.get_users_tweets(
                id=user_id,
                max_results=20,
                exclude=["retweets"],
                tweet_fields=["created_at", "public_metrics", "text"]
            )
            
            if not tweets.data:
                print(f"No se encontraron tweets para @{username}")
                continue
            
            # Procesar los tweets
            for tweet in tweets.data:
                tweet_data.append({
                    'usuario': username,
                    'texto': tweet.text,
                    'fecha': tweet.created_at,
                    'likes': tweet.public_metrics['like_count'],
                    'retweets': tweet.public_metrics['retweet_count']
                })
                
        except tweepy.errors.TweepyException as e:
            print(f"Error al procesar @{username}: {e}")
    
    return pd.DataFrame(tweet_data)

def main():
    # Autenticar
    api_client = authenticate()
    if not api_client:
        return
    
    # Obtener usuarios a analizar
    try:
        num_users = int(input("¿Cuántos usuarios quieres analizar? "))
        if num_users <= 0:
            print("Debes introducir un número positivo")
            return
    except ValueError:
        print("Debes introducir un número válido")
        return
    
    user_list = get_user_list(num_users)
    
    # Analizar tweets
    results = analyze_tweets(api_client, user_list)
    
    # Mostrar resultados
    if not results.empty:
        print("\nResultados del análisis:")
        print(results)
        
        # Guardar en CSV
        save_csv = input("¿Deseas guardar los resultados en un archivo CSV? (s/n): ").lower()
        if save_csv == 's':
            filename = input("Nombre del archivo (sin extensión): ")
            results.to_csv(f"{filename}.csv", index=False)
            print(f"Datos guardados en {filename}.csv")
    else:
        print("No se encontraron tweets para analizar")

if __name__ == "__main__":
    main()


          



     



	
