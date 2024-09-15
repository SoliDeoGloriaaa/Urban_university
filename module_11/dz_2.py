import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj)]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    obj_module = getattr(obj, '__module__', 'builtins' if obj_type in dir(__builtins__) else None)
    result = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }
    
    return result

number_info = introspection_info(42)
pprint.pprint(number_info)