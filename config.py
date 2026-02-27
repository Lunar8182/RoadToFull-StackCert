def add_setting(settings, key_val):
    key, val = key_val
    
    key = key.lower()
    val = val.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = val
        return f"Setting '{key}' added with value '{val}' successfully!"


def update_setting(settings, key_val):
    key, val = key_val

    key = key.lower()
    val = val.lower()

    if key in settings:
        settings[key] = val
        return f"Setting '{key}' updated to '{val}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key, val in settings.items():
            result += f"{key.capitalize()}: {val}\n"
        return result

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}


print(view_settings(test_settings))