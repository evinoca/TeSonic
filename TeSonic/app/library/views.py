from flask import render_template, redirect, request, url_for, flash ,jsonify
from flask.ext.login import login_user, logout_user, login_required
from . import library
from ..models import Product
from .forms import ImportForm


@library.route('/import',methods=['GET', 'POST'])
def importFile():
    form = ImportForm()
    if form.validate_on_submit():
        print form.title
        flash("importing file")
        flash(form.file.data)
        print form.file
    return render_template('library/import.html', form=form)

@library.route('/product',methods=['GET', 'POST'])
def productPage():
    products = Product.query.all()
    return render_template('library/product.html',products=products)

@library.route('/request',methods=['GET', 'POST'])
def requestPage():
    return render_template('library/request.html')

@library.route('/strategy',methods=['GET', 'POST'])
def strategyPage():
    return render_template('library/strategy.html')



@library.route('/ajax')
def y():
   if request.is_xhr:
       return jsonify({'count':'5'})
   return render_template('library/ajax.html')


@library.route('/bootstrap')
def bootstrapDemo():
   return render_template('library/bootstrap.html')