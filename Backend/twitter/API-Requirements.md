# Agents Page 

#### get agents

- request 
    - URL : ```/twitter/api/agents```
    - method : ```GET```
    

- response
    - type : JSON
    - Data : 
    ```JSON
    [
        {
            "name" : "" , // String
            "project": {  // Object
                "name" : "" ,// String 
                "color" : "" , // String like #ffff
                "imgURL" : "" , // String Img Path
            },
            "accounts_count" : 0 // Integer
            
        },
    ]
    ```


