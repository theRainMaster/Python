"""
Программа на Python для отслеживания курса валюты

"""
# импорт необходимых библиотек
import requests, json

# Функция для обмена валюты в реальном времени
def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) : 
  
    # base_url переменная store base url
    base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
  
    # main_url переменная хранит полный URL
    main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key 
  
    # получить метод модуля запросов
    # вернуть объект ответа
    req_ob = requests.get(main_url) 
  
    # метод json возвращает формат json
    # данные в тип данных Python Dictionary.
      
    # результат содержит список вложенных словарей
    result = req_ob.json() 
  
    print(" Result before parsing the json data :\n", result) 
  
      
    print("\n After parsing : \n Realtime Currency Exchange Rate for", 
          result["Realtime Currency Exchange Rate"] 
                ["2. From_Currency Name"], "TO", 
          result["Realtime Currency Exchange Rate"] 
                ["4. To_Currency Name"], "is", 
          result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'], to_currency) 
  
  
  
#
if __name__ == "__main__" : 
  
    # код валюты
    from_currency = "USD"
    to_currency = "RUB"
  
    # введите свой ключ API здесь
    api_key = "ULM8NS1SAX1M6GHV"
  
    # вызов функции
    RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) 
