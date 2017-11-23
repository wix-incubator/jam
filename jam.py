#!/usr/bin/env python3
import os, sys
from argparse import ArgumentParser, FileType
from yaml import safe_load as load
from jinja2 import Template


def main():
  parser = ArgumentParser()
  parser.add_argument('input', type=FileType('r'))
  parser.add_argument('output', nargs='?', type=FileType('w'), default=sys.stdout)
  args = parser.parse_args()
  result = jam(args.input)
  args.output.write(result)


def jam(input):
  config = load(input)
  template = Template(config['template'])
  return template.render(data=config['data'])


if __name__ == "__main__":
  if not os.isatty(0):
    print(jam(sys.stdin))
  else:
    main()
