from rest_framework.renderers import JSONRenderer

from status.models import Status
from status.api.serializers import StatusSerializer, CustomSerializer

'''Serialize a Single Object'''
obj = Status.objects.first()
serializer = StatusSerializer(obj)
serializer.data
json_data = JSONRenderer().render(serializer.data)
print(json_data)

'''Serialize a Query Set'''
qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

'''Create obj'''
data = {'user': 1}
serializer = StatusSerializer(data=data)
serializer.is_valid()

if serializer.is_valid():
    serializer.save()

'''Update obj'''
obj = Status.objects.first()  # grab the obj to update
data = {'content': 'some new content', 'user': 1}  # data to update
update_serializer = StatusSerializer(obj, data=data)
update_serializer.is_valid()

if update_serializer.is_valid():
    update_serializer.save()

'''Delete obj'''
data = {'user': 1, 'content': 'Please delete me'}
create_obj_serializer = StatusSerializer(data=data)
create_obj_serializer.is_valid()
create_obj = create_obj_serializer.save()  # returns instance of saved obj
print(create_obj)
print(create_obj.id)

obj = Status.objects.last()  # grab the recent obj to delete
get_data_serializer = StatusSerializer(obj)
print(get_data_serializer.data)
print(obj.delete())  # delete the object. No need of serializer to delete


data = {'email': 'hello@kiran.com', 'content': 'please delete me'}
create_obj_serializer = CustomSerializer(data=data)
if create_obj_serializer.is_valid():
    valid_data = create_obj_serializer.data
    print(valid_data)