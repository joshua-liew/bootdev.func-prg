def new_resizer(max_width, max_height):
    
    def set_min_size(min_width=0, min_height=0):
        if (min_width > max_width) or (min_height > max_height):
            raise Exception("minimum size cannot exceed maximum size")

        def set_width_and_height(width, height):
            new_width = width
            if width > max_width:
                new_width = min(width, max_width)
            if width < min_width:
                new_width = max(width, min_width)

            new_height = height
            if height > max_height:
                new_height = min(height, max_height)
            if height < min_height:
                new_height = max(height, min_height)

            return new_width, new_height

        return set_width_and_height

    return set_min_size
