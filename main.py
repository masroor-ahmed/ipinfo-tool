import requests

def get_ip_info(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}?token={token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.text)
        return None

def display_ip_info(ip_info):
    if ip_info:
        print("IP Information:")
        print("IP:", ip_info.get('ip'))
        print("Country:", ip_info.get('country'))
        print("Region:", ip_info.get('region'))
        print("City:", ip_info.get('city'))
        print("Postal Code:", ip_info.get('postal'))
        print("Coordinates:", ip_info.get('loc'))
        print("ISP:", ip_info.get('org'))
        print("ASN:", ip_info.get('asn'))
        print("Hostname:", ip_info.get('hostname'))
        print("Timezone:", ip_info.get('timezone'))
        print("Connection Type:", ip_info.get('connection_type'))
        print("Threat Level:", ip_info.get('threat_level'))

        abuse = ip_info.get('abuse')
        if abuse:
            print("Abuse Confidence Score:", abuse.get('confidence'))
        else:
            print("Abuse Confidence Score: Not available")
    else:
        print("IP information not available.")

def main():
    token = "fcc5cc5d435b70"  # Replace with your API token
    
    while True:
        ip_address = input("Enter the IP address: (type 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            break
        else:
            ip_info = get_ip_info(ip_address, token)
            display_ip_info(ip_info)

if __name__ == "__main__":
    main()
