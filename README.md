# Jekyll-mermaid-blog

A [Jekyll](http://jekyllrb.com/) blog integrated with the [mermaid](https://github.com/knsv/mermaid) library for diagrams and flowcharts in your posts and pages.

## Installation

1. Install [Jekyll](http://jekyllrb.com/)
2. Download repository

Please see the [Jekyll documentation](http://jekyllrb.com/docs/plugins/#installing-a-plugin) for more installation options.

## Config

The [mermaid](https://github.com/knsv/mermaid) javascript files are sourced through `_config.yml`.

```ruby
mermaid:
  src: '/js/mermaid.js'
  src_config: '/js/mermaid_config.js'
```

Publish the jekyll blog is done through the `RakeFile` so you will need to update the `GITHUB_REPONAME`.

## Usage

Running the jekyll site locally by executing jekyll serve.

```shell
jekyll serve
```

The website can be published by executing a rake command.

```shell
rake publish
````

For working with mermaid diagrams, simply include the [jekyll-mermaid](https://github.com/jasonbellamy/jekyll-mermaid) block helper in any of your templates.

```liquid
{% mermaid %}
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
{% endmermaid %}
```

Please see the [mermaid documentation](https://github.com/knsv/mermaid/wiki) for more examples.


## Demo

For a working example, check out the [blog post](http://quickinsights.io/apache/spark/apache-spark-redshift) as well the [source code](https://github.com/trienism/jekyll-mermaid-blog).
