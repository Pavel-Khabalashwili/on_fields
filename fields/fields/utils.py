import string
import random

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    ModelClass = instance.__class__
    qs_exists = ModelClass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
