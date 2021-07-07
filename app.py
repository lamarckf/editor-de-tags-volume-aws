import boto3
from chalice import Chalice
import string
ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')

app = Chalice(app_name='test_rename_tags_volume') #Rever a permissão que é criada, adicionar ec2

@app.on_cw_event({"source": ["aws.ec2"]})

def tags_resource_find(event):
    body=event.to_dict()
    resources=str(body['resources'])
    detail=str(body['detail'])
    test_status=detail[47:-56]
    test_volume=resources[37:-2] #alterar dependendo da região utilizada
    newVolume=test_volume[7:]
    service=test_volume[0:6]
    if service == 'volume':
        if test_status == 'createVolume':
            volumes = ec2.volumes.all() 
            for volume in volumes:
                auxVolume=str(volume)
                verificadorVolume=auxVolume[15:-2]
                if verificadorVolume == newVolume:
                    volume.create_tags(Tags=[{'Key': 'exemplo', 'Value': 'value exemplo'}])
                    volume.create_tags(Tags=[{'Key': 'exemplo2', 'Value': 'value exemplo'}])
                    volume.create_tags(Tags=[{'Key': 'exemplo3', 'Value': 'value exemplo'}])
                    volume.create_tags(Tags=[{'Key': 'exemplo4', 'Value': 'value exemplo'}])
                    volume.create_tags(Tags=[{'Key': 'exemplo5', 'Value': 'value exemplo'}])


