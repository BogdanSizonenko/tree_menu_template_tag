from django import template
from ..models import Option


register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu):
    # Отрисовываем меню
    result_dict = {
        'options': [
            option for option in Option.objects.filter(menu__title=menu, parent_option=None).values()
        ]
    }
    parent_option_id = \
        [option['id'] for option in Option.objects.filter(menu__title=menu, child_option__isnull=False).values()]
    for option in result_dict['options']:
        if option['id'] in parent_option_id:
            option['child_options'] = get_child_options(option, menu, parent_option_id)
    
    result_dict['menu'] = menu    
    result_dict['url_string'] = get_url_string(context, menu)
    return result_dict

# Получаем подопции строчек меню
def get_child_options(option, menu, parent_option_id):
    child_options = \
        [option for option in Option.objects.filter(menu__title=menu, parent_option_id=option['id']).values()]
    for option in child_options:
        if option['id'] in parent_option_id:
            option['child_options'] = get_child_options(option, menu, parent_option_id)
    return child_options

# Url адрес для пункта меню
def get_url_string(context, menu):
    list_args = []
    for key in context['request'].GET:
        if key != menu:
            list_args.append(key + '=' + context['request'].GET[key])
    url_string = ('&').join(list_args)
    return url_string