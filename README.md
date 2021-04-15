# Pero por suerte es viernes

## Requirements

- `python3.8`
- `zip`


### Pip requriements
```
pip install -r requirements.txt
```



## Prepare for deployment

### Zip requirements

Install requirements locally
```
pip install -r requirements.txt -t python/lib/python3.8/site/packages/
```

Zip requirements
```
zip -r requirements.zip python
```

## Create a lambda layer
After we've created the zip with the requirements, 
we need to [create a new lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-create) 
using the requirements zip file.


## Zip source code
```
zip -r viernes.zip viernes/*.py
```


## Upload source code zip file to lambda function
Load the zip file we've just created to the lambda function.
Replace the controller with `app.lambda_handler`.


## Configure the environment variables
Follow the `.env.template` file to configure in 
lambda the environment variables needed for the 
correct functioning of the code.


## Configure cron with CloudWatch
On AWS, go to CloudWatch, Events, Rules.
Create a new rule with a cron expression
that points to the desired lambda function.