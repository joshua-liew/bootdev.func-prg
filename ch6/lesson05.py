import copy


def css_styles(initial_styles):
    styles = copy.deepcopy(initial_styles)

    def add_styles(selector, property, value):
        if selector not in styles:
            new_dict = {
                selector: {
                    property: value,
                },
            }
            styles.update(new_dict)
        else:
            styles[selector][property] = value
        return styles

    return add_styles
