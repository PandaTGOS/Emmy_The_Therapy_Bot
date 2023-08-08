import json

data=json.load(open('./intents.json'))

with open("data.text","a") as fh:
    for i in data['intents']:
        x=i['responses']
        y=i['patterns']
        print(x,"\n",y)
        fh.write("response(\""+str(x[0])+"\","+str(y)+")\n")
