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
    - name: React Native
      links:
        - title: Flexbox
          url: https://facebook.github.io/react-native/docs/flexbox.html
        - title: Running On Device
          url: https://facebook.github.io/react-native/docs/running-on-device.html
        - title: Flatlist
          url: https://facebook.github.io/react-native/docs/flatlist.html

    - name: Monitoring
      links:
        - title: New Relic
          url: https://newrelic.com/
        - title: Sentry
          url: https://sentry.io/

template:
  url: https://raw.githubusercontent.com/wix/jam/master/templates/overengineered-home.html.j2

```

## License

The MIT License (MIT)
