from django import template


register = template.Library()


@register.filter()
def display_name(queryset, index):
  model_object = queryset[index].name  
  return model_object

@register.filter()
def display_image(queryset, index):
  model_object = queryset[index].display_image.url
  return model_object

    
 
