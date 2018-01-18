# jam

A tool for generating static HTML files. Basic setup allows to specify Jinja template and values that drive
that template in a single yaml file.

Advanced options:
  * include CSS files into final HTML file
  * specify template using url instead of inside yaml

Useful for generating homepage for Safari or a simple one page site.

## Usage

Create a yaml file on your machine (see samples below), run jam.py to generate HTML file.

```
python3 jam.py path/to/page.yaml path/to/home.html
```

## Basic sample

```yaml
data:
  title: GitHub projects
  links:
    - title: A complete native navigation solution for React Native
      url: https://github.com/wix/react-native-navigation
    - title: React Native Calendar Components
      url: https://github.com/wix/react-native-calendars

template:
  <!doctype html>
  <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>{{data.title}}</title>
    </head>
    <body>
      <h1>{{data.title}}</h1>
      {% for link in data.links %}
      <br><a href="{{link.url}}">{{link.title}}</a>
      {% endfor %}
    </body>
  </html>
```


## Complex sample
```yaml
data:
  title: Home
  groups:
    - name: Repositories
      links:
        - title: WOA engine
          url: https://github.com/wix-private/wix-one-app-engine
        - title: UI Lib (public)
          url: https://github.com/wix/react-native-ui-lib/
        - title: UI Lib (Wix)
          url: 'https://github.com/wix-private/wix-react-native-ui-lib/'

    - name: Deployment
      links:
        - title: POCO
          url: https://bo.wix.com/wix-poco#/
        - title: Team City
          url: http://tc.dev.wixpress.com/

    - name: Monitoring
      links:
        - title: New Relic
          url: https://newrelic.com/

template:
  url: https://raw.githubusercontent.com/wix/jam/master/templates/overengineered-home.html.j2

```

## License

The MIT License (MIT)
