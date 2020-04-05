# HomeHub-Django
Repository for db functionalities for HomeHub

# Steps to run

Clone the repository
- Run `python manage.py migrate`
- Run `python manage.py runserver`

# APIS

## Get authentication token
- Endpoint: ```http://localhost:8000/api-token-auth/```
  - Parameters required : ```username, password```
  - Sample body:
  ```json
  {
    "username": "admin",
    "password": "password"
  }
  ```

## Get / Post user
- Endpoint : ```http://localhost/api/user/```
- GET
  - parameters: ```auth token as header```
  - sample header:
  ```json
  {
    "Authorization": "TOKEN <token>"
  }
  ```
  - sample response:
  ```json
  {
    "username": "<username>",
    "first_name": "<first_name>",
    "last_name": "<last_name>",
    "email": "<email>",
    "password": "<encrypted string>"
   }
   ```
- POST
  - parameters:
    - header: ```auth token as header```
    - sample:
      ```json
      {
        "Authorization" : "TOKEN <token>"
      }
      ```
    - ```username, email, first_name, last_name, password```
    - sample:
    ```json
    {
      "username": "<username>",
      "first_name": "<first_name>",
      "last_name": "<last_name>",
      "email": "<email>",
      "password": "<encrypted string>"
     }
     ```
   - response (on succesful):
    ```json
    {
      "message": "created succesfully"
    }
   ```

# Utils
## QR-Code
- To generate:
  ```python
  from utils.qr_code_utils import generate_qr_code
  from PIL import Image
  
  image = generate_qr_code("test")
  image = Image.fromarray(image)
  # View the image
  image.show()
  image.save("hello.png")
  
  ```
- To decode:
  ```python
  from utils.qr_code_utils import decode_qr_code
  from PIL import Image
  import numpy as np
  
  image = Image.open("test.png")
  image_np = np.array(image)
  print(decode_qr_code(image_np=image_np))  
  ```