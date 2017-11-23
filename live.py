#!/usr/bin/env python3
from argparse import ArgumentParser
from flask import Flask
from os import path
from jam import jam


def main():
  parser = ArgumentParser()
  parser.add_argument('dir')
  args = parser.parse_args()
  instance_path = path.abspath(args.dir)
  static_folder = path.join(instance_path, 'static')
  app = Flask(__name__, instance_path=instance_path, static_folder=static_folder)

  @app.route('/')
  def home():
    return 'Add file to address'

  @app.route('/<file>')
  def preview(file):
    source = path.join(app.instance_path, file)
    return jam(open(source, 'r'))

  app.run(debug=True)


if __name__ == "__main__":
  main()
