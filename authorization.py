import tekore as tk

def auth():
  client_id  = "x"
  secret_key = "x"
  token = tk.request_client_token(client_id, secret_key)
  return tk.Spotify(token)