from ..base.renderer import BaseRenderer

class RaspbianRenderer(BaseRenderer):

    def get_name(self):
        renderers = []
        for cls in RaspbianRenderer.__subclasses__():
            renderers.append(cls.__name__)
        return renderers

    def render(self):
        output = ''
        for file_name in RaspbianRenderer.get_name(self):
            template_name = '{0}.jinja2'.format(file_name)
            template = BaseRenderer.template_env.get_template(template_name)
            context = getattr(BaseRenderer.backend, 'intermediate_data', {})
            partial_output = template.render(data=context)
            output += partial_output
        return self.cleanup(output)


class Hostname(RaspbianRenderer):
    pass


class Hostapd(RaspbianRenderer):
    pass


class Interfaces(RaspbianRenderer):
    pass


class Resolv(RaspbianRenderer):
    pass


class Ntp(RaspbianRenderer):
    pass
