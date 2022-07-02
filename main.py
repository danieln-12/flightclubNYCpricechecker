import requests
import json


headers = {
    'authority': 'sell.flightclub.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://sell.flightclub.com/sell',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

def main():
    name = input('Search Query:\n')
    params = {
    'page': '1',
    'perPage': '20',
    'query': name,
}
    response = requests.get('https://sell.flightclub.com/api/public/search', params=params, headers=headers)
    response = response.json()
    id = response['results'][0]['id']
    prod_data = requests.get(f'https://sell.flightclub.com/api/public/products/{id}', headers=headers)
    prod_data = prod_data.json()
    
    item = prod_data["name"]
    image = prod_data["imageUrl"]
    id = prod_data["id"]
    sku = prod_data["style"]
    print(f'Product => {item}')
    print(f'SKU => {sku}')
    print(f'ID => {id}')
    sizes = ['4','4.5','5','5.5','6','6.5','7','7.5','8','8.5','9','9.5','10','10.5','11','11.5','12','12.5','13','14']
    gs_sizes = ['4Y','4.5Y','5Y','5.5Y','6Y','6.5Y','7Y']
    wmns_sizes = ['w5','w5.5','w6','w6.5','w7','w7.5','w8','w8.5','w9','w9.5','w10','w10.5','w11','w11.5','w12']
    division = prod_data['division']
    x = ''
    if division == "Men":
        for x in sizes:
            price = prod_data['suggestedPrices'][x]['lowestConsignedPriceCents']
            if price == None:
                print(f'Size {x} US => N/A')
            else:
                payout = ((0.905 * price) - 500 ) *0.971
                print(f'Size => {x} US | Price => {price/100:.2f} | Payout => {payout/100:.2f}') 


    if division == "Women":
        for x in wmns_sizes:
            price = prod_data['suggestedPrices'][x]['lowestConsignedPriceCents']
            if price == None:
                print(f'Size {x} US => N/A')
            else:
                payout = ((0.905 * price) - 500 ) *0.971
                print(f'Size => {x} US | Price => {price/100:.2f} | Payout => {payout/100:.2f}')    

    if division == "Boy":
        for x in gs_sizes:
            price = prod_data['suggestedPrices'][x]['lowestConsignedPriceCents']
            if price == None:
                print(f'Size {x} US => N/A')
            else:
                payout = ((0.905 * price) - 500 ) *0.971
                print(f'Size => {x} US | Price => {price/100:.2f} | Payout => {payout/100:.2f}')    

    
main()
