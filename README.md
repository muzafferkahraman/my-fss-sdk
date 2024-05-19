# my-fss-sdk

I set out to simplify the API coding process for FSS. This **project is still ongoing** and I'm **adding new APIs whenever I find the opportunity**.
Instead of dealing with a more comprehensive API using the requests library, I aimed to abstract the process into concise and understandable methods.
ie to get a list of regions, we first need to get an Authentication token: <br>

> headers={'Content-Type': 'application/json'} <br>
> data='{"username":"admin","password":"NokiaFss1!"}' <br>
> res = requests.post(self.host+'/rest/auth/login', headers=headers, data=data, verify=False) <br>
> token=res.json()['access_token'] <br>

Then with the token we need to send a request to get the regions <br>
> headers={'Authorization':'Bearer {}'.format(token)} <br>
> result = requests.get(self.host+'/rest/intentmgr/api/v1/regions', headers=headers,verify=False).json() <br>


To simplify the process, importing my-fss-sdk.FSS you just code the whole process as

> session.get_regions()

Moreover if you know and specify the name of the region, you can just refer it and get just the relevant region

> session.get_regions(region_name)

Moreover, in that case the API will return you not only the objecty but also the uuid of the object, with a dictionary format

{"content":region,"id":region_id}

Of course id can be retrieved from the region object itself, however at times it will be handy to get this value easily, when you are referring the id as the parent object.





