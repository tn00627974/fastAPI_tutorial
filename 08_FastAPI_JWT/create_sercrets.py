import secrets

SECRET_KEY = secrets.token_urlsafe(32)

print(SECRET_KEY)

# 32字節的密鑰提供256位隨機數據，這是一個安全的密鑰，可以用於加密數據。
# 用於 JWT 密鑰來簽署驗證
