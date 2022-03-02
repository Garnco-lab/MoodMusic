import tekore as tk

def auth():
_
  token = tk.request_client_token(client_id, secret_key)
  return tk.Spotify(token)