# How to eable developer options

## The problem: 

To get developer, you got to *Settings --> About Device --> click TUSN multile times*

You will be prompted to enter s 4-digit verification code, that is checked by this endpoint:

```
http://api.sunmi.com/api/financial/app/financial/1.1/?service=/checkauthcode

```

The response will be:

```
{"code":-1,"data":null,"msg":""}
```

# Mitmproxy

- cd into this folder https://github.com/flowluap/sunmi/edit/master/scripts

- and run ````mitmdump -s proxy.py```

- this will fake the server response.

- unfortunately there is some kind of check in the data part, that maybe has to do something with this file here: https://github.com/wenzhenxi/phalgo/blob/22606d9dd248e7913abc4530e51241d71aca236c/des.go

- Some kind of MD5 hash with signature.

![IMG_20200803_023005](https://user-images.githubusercontent.com/49984289/89136444-1bd23c80-d534-11ea-87a5-028299108c39.jpg)
