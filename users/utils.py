from django.core.exceptions import ValidationError


def validate_image_size(value):
    max_size = 2 * 1024 * 1024  # 2 MB
    if value.size > max_size:
        raise ValidationError("La imagen no debe superar los 2 MB.")