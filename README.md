# jam

A tool to produce html out of data and template specified in a single yaml file. Useful for generating homepage for Safari or a simple one page site.

## Sample

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

## License

The MIT License (MIT)
