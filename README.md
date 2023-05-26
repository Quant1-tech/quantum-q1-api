# quantum-q1-api
Financial market quantitative methods API
# Quantum - Q1 tutorial

#### Repository dedicated to Quantum API usage instructions.

## Authentication

Our services work throung a dual authentication system, using a user token provided by the Rapid platform, and through Quantum's authentication provider. To get token our provider, you must go to the following link <https://provider.quant1.com.br/>, where you must register or log in if already have an account. After logging in, you will directed to the proovider's homepage. Here is where you manage your clients. 

To get an authorization token, you must create a client of type Client Credentials Grand. Do this by following these steps:

1. click the button to create a new client. You will be directed to our creation client.
2. The client name field can be filled in at your choice;
3. The allowed scope field must be filled as **profile;**
4. The allowed grand types field must be filled as **password;**
5. The client uri, redirect uri and allowed response types can be left blank for the client credentials type.
6. The token endpoint auth method field can be changed between client_secret_basic and client_secret_post, where respectively the client uses HTTP basic authentication and HTTP POST parameters.

When hen creating a client you will have acquired client_id and client_secret. With this data you will get a token through a terminal, or by executing some HTTP algorithm in a programming language of your choice. Here's an example using the curl tool:

```
curl -u {client_id}:{client_secret} -XPOST https://provider.quant1.com.br/oauth/token -F grant_type=password -F username={username} -F password={password} -F scope=profile
```

Se os dados inseridos forem compativéis com o o seu client, você tera uma resposta em json contendo o token de autorização no formato bearer:

```
{"access_token": "acess_token", "expires_in": "expires_in", "refresh_token": "refresh_token", "scope": "scope", "token_type": "Bearer"}
```
