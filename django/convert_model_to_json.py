from django.forms.models import model_to_dict

def convert_model_to_json(model_object):
    dict_obj = model_to_dict(model_object)
    serialized_json = json.dumps(dict_obj)
    return serialized_json
