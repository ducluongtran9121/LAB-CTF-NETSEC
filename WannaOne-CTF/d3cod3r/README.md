# D3COD3R

## SSTI discovery

- Chúng ta phát hiện được rằng chương trình có lỗ hỏng [SSTI](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#jinja2-python) khi truyển chuỗi Base64 `e3snYScudXBwZXJ9fQ==` ( {{'a'.upper}} ) vào Decoder field của chương trình
