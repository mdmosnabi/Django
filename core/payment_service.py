import requests
import datetime
from django.conf import settings

class BkashService:
    def __init__(self):
        self.base_url = settings.BKASH_BASE_URL
        self.app_key = settings.BKASH_APP_KEY
        self.app_secret = settings.BKASH_APP_SECRET
        self.username = settings.BKASH_USERNAME
        self.password = settings.BKASH_PASSWORD
        self.token = self.get_access_token()
        self.refresh_token = None

    def get_access_token(self):
        url = f"{self.base_url}/checkout/token/grant"
        auth = (self.username, self.password)
        headers = {"X-App-Key": self.app_key}
        payload = {
            "app_key": self.app_key,
            "app_secret": self.app_secret,
        }
        response = requests.post(url, auth=auth, headers=headers, json=payload)
        response_data = response.json()
        self.refresh_token = response_data.get("refresh_token")
        return response_data.get("id_token")

    def refresh_access_token(self):
        url = f"{self.base_url}/checkout/token/refresh"
        auth = (self.username, self.password)
        headers = {"X-App-Key": self.app_key}
        payload = {
            "app_key": self.app_key,
            "app_secret": self.app_secret,
            "refresh_token": self.refresh_token,
        }
        response = requests.post(url, auth=auth, headers=headers, json=payload)
        response_data = response.json()
        self.token = response_data.get("id_token")
        self.refresh_token = response_data.get("refresh_token")
        return self.token

    def create_payment(self, amount, invoice_number):
        url = f"{self.base_url}/checkout/payment/create"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "X-App-Key": self.app_key,
        }
        payload = {
            "amount": amount,
            "currency": "BDT",
            "intent": "sale",
            "merchantInvoiceNumber": invoice_number,
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 401:
            self.get_access_token()  # Refresh token
            headers["Authorization"] = f"Bearer {self.token}"
            response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def execute_payment(self, payment_id):
        url = f"{self.base_url}/checkout/payment/execute/{payment_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "X-App-Key": self.app_key,
        }
        response = requests.post(url, headers=headers)
        return response.json()

    def refund_payment(self, payment_id, amount, trx_id, reason="Product Return"):
        url = f"{self.base_url}/checkout/payment/refund"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
            "X-App-Key": self.app_key,
        }
        payload = {
            "paymentID": payment_id,
            "amount": str(amount),
            "trxID": trx_id,
            "sku": "REFUND",
            "reason": reason,
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
    
