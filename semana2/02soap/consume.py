from zeep import Client

client = Client("https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL")
result = client.service.NumberToDollars(100)  # Puedes cambiar el número según sea necesario
print(result)
