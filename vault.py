from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential


KVUri = "https://synelab.vault.azure.net/"
secretName = "creds"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)
retrieved_secret = client.get_secret(secretName)

print(f"The value of secret '{secretName}' is: '{retrieved_secret.value}'")
