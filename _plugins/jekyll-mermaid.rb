module Jekyll
  class Mermaid < Liquid::Block

    def initialize(tag_name, markup, tokens)
      super
    end

    def render(context)
      @config = context.registers[:site].config['mermaid']
      "<div class=\"mermaid\" id=\"i141\">#{super}</div>"
    end
  end
end

Liquid::Template.register_tag('mermaid', Jekyll::Mermaid)
