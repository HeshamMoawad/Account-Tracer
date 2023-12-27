# Agents Page 

#### get agents

you can use this endpoint for get agents list of get list with filters of project names 

- request  
    - URL : ```/twitter/api/agents```
    - method : ```GET```
    - params : * Optional
    ```json
    {
        //must be list - default null or (not send)to get all agents
        "filter" : ["example"] 
    }
    ```

- response
    - type : JSON
    - Data : 
    ```json
    [   // emty list if filter is null or not sended
        {
            "name" : "" ,  // String
            "project": {   // Object
                "name" : "" , // String 
                "color" : "" , // String like #ffff
                "imgURL" : "" , // String Img Path
            },
            "accounts_count" : 0 // Integer
        },
    ]


    [] // empty list if filter = [] will return empty list
    ```


