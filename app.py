import sqlite3

from flask import Flask, flash, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/blogs")
def blogs():

    return render_template("blogs.html")

@app.route("/about-me")
def blogs():

    return render_template("about-me.html")

@app.route("/contact")
def blogs():

    return render_template("contact.html")

@app.route("/homepage")
def blogs():

    return render_template("homepage.html")

@app.route("/projects")
def blogs():

    return render_template("projects.html")

@app.route("/resume")
def blogs():

    return render_template("resume.html")


