from flask import Flask, render_template, url_for, redirect
from app_blog import app

if __name__ == '__main__':
    app.debug = True
    app.run()
